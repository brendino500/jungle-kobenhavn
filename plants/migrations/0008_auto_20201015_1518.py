# Generated by Django 3.1.2 on 2020-10-15 15:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0007_plant_basketid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='plant',
            old_name='basketID',
            new_name='basket',
        ),
    ]