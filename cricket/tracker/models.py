from django.db import models
from django.urls import reverse
from phone_field import PhoneField

# Create your models here.

class Todo(models.Model):
    todoTime = models.DateTimeField()
    task = models.CharField(max_length=255)
    lastDone = models.DateTimeField(blank=True)
    recurring = models.BooleanField(default=False)

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of a task.
        """
        return reverse('task-detail', args=[str(self.id)])  # task-detail comes form URlS.py

    def __str__(self):
        return self.task

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
        return reverse('supplier-detail', args=[str(self.id)])  # supplier-detail comes form URlS.py

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
    supplier_id = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    lastDelivery = models.DateField(blank=True)
    nextDelivery = models.DateField(blank=True)
    deliveryFrequency = models.CharField(max_length=35, blank=True)

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of a supply.
        """
        return reverse('supply-detail', args=[str(self.id)])  # supply-detail comes form URlS.py

    def __str__(self):
        return self.description

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
        return reverse('appt-detail', args=[str(self.id)])  # appt-detail comes form URlS.py

    def __str__(self):
        return '%s %s' % (self.dateTime, self.seeing)

    class Meta:
        # order appt by dateTime
        ordering = ['dateTime']