# Generated by Django 3.1.2 on 2020-10-15 10:41

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jwt_auth', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='orders',
            field=models.ManyToManyField(blank=True, related_name='orders_made', to=settings.AUTH_USER_MODEL),
        ),
    ]