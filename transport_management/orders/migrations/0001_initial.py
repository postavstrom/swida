# Generated by Django 5.1.2 on 2024-10-12 20:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(max_length=100)),
                ('customer_name', models.CharField(max_length=100)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Waypoint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_name', models.CharField(max_length=200)),
                ('waypoint_type', models.CharField(choices=[('pickup', 'Pickup'), ('delivery', 'Delivery')], max_length=50)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='waypoints', to='orders.order')),
            ],
        ),
    ]
