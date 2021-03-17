# Generated by Django 3.1.7 on 2021-03-17 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0011_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='provider',
            field=models.CharField(choices=[('@txt.att.net', 'AT&T'), ('@tmomail.net', 'T-Mobile'), ('@messaging.sprintpcs.com', 'Sprint'), ('@vtext.com', 'Verizon'), ('OTHER', 'Other')], default='T-Mobile', max_length=30),
        ),
    ]