# Generated by Django 3.1.5 on 2021-02-13 07:26

from django.db import migrations, models
import django.db.models.deletion
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0002_appointments_supplier_supplies'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
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
            name='Supply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=40)),
                ('orderNumber', models.CharField(max_length=30)),
                ('category', models.CharField(choices=[('RESP', 'Respiratory'), ('FEED', 'Feeding'), ('MEDS', 'Medication'), ('WOUND', 'Wound Care'), ('OTHER', 'Other')], max_length=30)),
                ('amount', models.PositiveIntegerField()),
                ('lastDelivery', models.DateField()),
                ('nextDelivery', models.DateField()),
                ('deliveryFrequency', models.CharField(max_length=35)),
            ],
            options={
                'ordering': ['description'],
            },
        ),
        migrations.DeleteModel(
            name='Appointments',
        ),
        migrations.RemoveField(
            model_name='supplier',
            name='supplier_id',
        ),
        migrations.RemoveField(
            model_name='todo',
            name='tid',
        ),
        migrations.DeleteModel(
            name='Supplies',
        ),
        migrations.AddField(
            model_name='supply',
            name='supplier_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracker.supplier'),
        ),
    ]