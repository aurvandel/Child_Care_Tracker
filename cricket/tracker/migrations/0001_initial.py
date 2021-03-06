# Generated by Django 3.1.5 on 2021-02-02 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tid', models.PositiveIntegerField(unique=True)),
                ('todoTime', models.DateTimeField()),
                ('task', models.CharField(max_length=255)),
                ('lastDone', models.DateTimeField()),
            ],
            options={
                'ordering': ['todoTime'],
            },
        ),
    ]
