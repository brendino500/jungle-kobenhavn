# Generated by Django 3.1.2 on 2020-10-15 15:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basket', '0004_auto_20201015_1517'),
        ('plants', '0006_remove_plant_basketid'),
    ]

    operations = [
        migrations.AddField(
            model_name='plant',
            name='basketID',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='basket.basket'),
            preserve_default=False,
        ),
    ]
