# Generated by Django 3.1.5 on 2021-02-03 00:22

from django.db import migrations, models
import django.db.models.deletion
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appt_id', models.PositiveIntegerField(unique=True)),
                ('dateTime', models.DateTimeField()),
                ('seeing', models.CharField(max_length=35)),
                ('address', models.CharField(max_length=35)),
                ('phone', phone_field.models.PhoneField(blank=True, max_length=31)),
            ],
            options={
                'ordering': ['dateTime'],
            },
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supplier_id', models.PositiveIntegerField(unique=True)),
                ('name', models.CharField(max_length=35)),
                ('phone', phone_field.models.PhoneField(blank=True, help_text='Company phone number', max_length=31)),
                ('afterHoursPhone', phone_field.models.PhoneField(blank=True, help_text='On call number', max_length=31)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Supplies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supply_id', models.PositiveIntegerField(unique=True)),
                ('description', models.CharField(max_length=40)),
                ('orderNumber', models.CharField(max_length=30)),
                ('category', models.CharField(choices=[('RESP', 'Respiratory'), ('FEED', 'Feeding'), ('MEDS', 'Medication'), ('WOUND', 'Wound Care'), ('OTHER', 'Other')], max_length=30)),
                ('amount', models.PositiveIntegerField()),
                ('lastDelivery', models.DateField()),
                ('nextDelivery', models.DateField()),
                ('deliveryFrequency', models.CharField(max_length=35)),
                ('supplier_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracker.supplier')),
            ],
            options={
                'ordering': ['description'],
            },
        ),
    ]
