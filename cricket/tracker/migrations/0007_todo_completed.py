# Generated by Django 3.1.5 on 2021-02-14 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0006_auto_20210213_2157'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='completed',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
