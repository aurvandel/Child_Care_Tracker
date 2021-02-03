from django.db import models
from django.urls import reverse
from phone_field import PhoneField

# Create your models here.

class Todo(models.Model):
    tid = models.PositiveIntegerField(unique=True)
    todoTime = models.DateTimeField()
    task = models.CharField(max_length=255)
    lastDone = models.DateTimeField()

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
    supplier_id = models.PositiveIntegerField(unique=True)
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

class Supplies(models.Model):
    CATEGORIES = (
        ('RESP', 'Respiratory'),
        ('FEED', 'Feeding'),
        ('MEDS', 'Medication'),
        ('WOUND', 'Wound Care'),
        ('OTHER', 'Other'),
    )
    supply_id = models.PositiveIntegerField(unique=True)
    description = models.CharField(max_length=40)
    orderNumber = models.CharField(max_length=30)
    category = models.CharField(max_length=30, choices=CATEGORIES)
    amount = models.PositiveIntegerField()
    supplier_id = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    lastDelivery = models.DateField()
    nextDelivery = models.DateField()
    deliveryFrequency = models.CharField(max_length=35)

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

class Appointments(models.Model):
    appt_id = models.PositiveIntegerField(unique=True)
    dateTime = models.DateTimeField()
    seeing = models.CharField(max_length=35)
    address = models.CharField(max_length=35)
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