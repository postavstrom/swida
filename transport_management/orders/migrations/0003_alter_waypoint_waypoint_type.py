# Generated by Django 5.1.2 on 2024-10-14 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_alter_order_order_number_alter_waypoint_order_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='waypoint',
            name='waypoint_type',
            field=models.CharField(choices=[('Pickup', 'Pickup'), ('Delivery', 'Delivery')], max_length=20),
        ),
    ]
