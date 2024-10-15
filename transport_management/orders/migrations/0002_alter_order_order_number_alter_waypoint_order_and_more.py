# Generated by Django 5.1.2 on 2024-10-13 16:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_number',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='waypoint',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='waypoints', to='orders.order'),
        ),
        migrations.AlterField(
            model_name='waypoint',
            name='waypoint_type',
            field=models.CharField(choices=[('Pickup', 'Pickup'), ('Delivery', 'Delivery')], max_length=10),
        ),
    ]
