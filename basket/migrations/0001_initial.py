# Generated by Django 3.1.2 on 2020-10-15 10:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('plants', '0002_plant_customer'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='User_orders', to='plants.plant')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='User_orders', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
