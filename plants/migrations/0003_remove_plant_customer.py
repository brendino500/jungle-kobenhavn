# Generated by Django 3.1.2 on 2020-10-15 13:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0002_plant_customer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plant',
            name='customer',
        ),
    ]
