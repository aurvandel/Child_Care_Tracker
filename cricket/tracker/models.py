from django.db import models
from django.urls import reverse
from phone_field import PhoneField
from django.utils import timezone
import datetime
import string

# Create your models here.

class Todo(models.Model):
    todoTime = models.DateTimeField()
    task = models.CharField(max_length=255)
    lastDone = models.DateTimeField(blank=True, null=True)
    recurring = models.BooleanField(default=False, blank=True)
    completed = models.BooleanField(default=False, blank=True)
    messageSent = models.BooleanField(default=False, blank=True)

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of a task.
        """
        return reverse('todo-detail', kwargs={'pk':self.pk})  # task-detail comes form URlS.py

    def __str__(self):
        return self.task

    def getDate(self):
        return self.todoTime.strftime('%x')

    def getTime(self):
        return self.todoTime.strftime('%X')

    @property
    def pastDue(self):
        return timezone.now() > self.todoTime

    @property
    def getCompleted(self):
        return self.completed

    @property
    def updateTodo(self):
        self.lastDone = self.todoTime
        self.todoTime += datetime.timedelta(days=1)

    @property
    def updateMessageSent(self):
        if self.messageSent:
            self.messageSent = False
        else:
            self.messageSent = True

    class Meta:
        # order tasks by time
        ordering = ['todoTime']

class Supplier(models.Model):
    name = models.CharField(max_length=35)
    phone = PhoneField(blank=True, help_text='Company phone number')
    afterHoursPhone = PhoneField(blank=True, help_text='On call number')

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of a supplier.
        """
        return reverse('supplier-detail', kwargs={'pk':self.pk})  # supplier-detail comes form URlS.py

    def __str__(self):
        return self.name

    class Meta:
        # order suppliers by name
        ordering = ['name']

class Supply(models.Model):
    CATEGORIES = (
        ('RESP', 'Respiratory'),
        ('FEED', 'Feeding'),
        ('MEDS', 'Medication'),
        ('WOUND', 'Wound Care'),
        ('OTHER', 'Other'),
    )
    description = models.CharField(max_length=40)
    orderNumber = models.CharField(max_length=30, blank=True)
    category = models.CharField(max_length=30, choices=CATEGORIES)
    amount = models.PositiveIntegerField(blank=True)
    supplier_id = models.ForeignKey(Supplier, on_delete=models.CASCADE, blank=True)
    lastDelivery = models.DateField(blank=True)
    nextDelivery = models.DateField(blank=True)
    deliveryFrequency = models.PositiveIntegerField(blank=False)

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of a supply.
        """
        return reverse('supply-detail', kwargs={'pk':self.pk})  # supply-detail comes form URlS.py

    def __str__(self):
        return self.description

    @property
    def pastDue(self):
        return datetime.date.today() > (self.lastDelivery + datetime.timedelta(days=self.deliveryFrequency))

    @property
    def updateSupplyDate(self):
        self.lastDelivery = datetime.date.today()
        self.nextDelivery = datetime.date.today() + datetime.timedelta(days=self.deliveryFrequency)
        print(self.nextDelivery)
        print(self.lastDelivery)

    class Meta:
        # order supplies by description
        ordering = ['description']

class Appointment(models.Model):
    dateTime = models.DateTimeField()
    seeing = models.CharField(max_length=35)
    address = models.CharField(max_length=35, blank=True)
    phone = PhoneField(blank=True)

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of a appt.
        """
        return reverse('appt-detail', kwargs={'pk':self.pk})  # appt-detail comes form URlS.py

    def __str__(self):
        return '%s %s' % (self.dateTime, self.seeing)

    class Meta:
        # order appt by dateTime
        ordering = ['dateTime']

class Contact(models.Model):
    
    CATEGORIES = (
        ('@txt.att.net', 'AT&T'),
        ('@tmomail.net', 'T-Mobile'),
        ('@messaging.sprintpcs.com', 'Sprint'),
        ('@vtext.com', 'Verizon'),
        ('OTHER', 'Other'),
    )
    name = models.CharField(max_length=35)
    phone = PhoneField(blank=False)
    provider = models.CharField(max_length=30, choices=CATEGORIES, default='T-Mobile')


    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of a contact.
        """
        return reverse('contact-detail', kwargs={'pk':self.pk})  # contact-detail comes form URlS.py

    def __str__(self):
        return '%s %s' % (self.name, self.phone)

    def getEmail(self):
        phone = str(self.phone)
        badChars = ["(", ")", " ", "-"]
        delete_dict = {sp_character: '' for sp_character in string.punctuation}
        delete_dict[' '] = ''
        table = str.maketrans(delete_dict)
        phone = phone.translate(table) 
        return '%s%s' % (str(phone), self.provider)

    class Meta:
        # order contacts by name
        ordering = ['name']