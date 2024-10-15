# orders/models.py

from django.db import models

class Order(models.Model):
    order_number = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=100)
    date = models.DateField()

    def __str__(self):
        return f"Order {self.order_number} for {self.customer_name}"

class Waypoint(models.Model):
    PICKUP = 'pickup'
    DELIVERY = 'delivery'
    WAYPOINT_TYPE_CHOICES = [
        (PICKUP, 'pickup'),
        (DELIVERY, 'delivery'),
    ]

    order = models.ForeignKey(Order, related_name='waypoints', on_delete=models.CASCADE)
    location_name = models.CharField(max_length=200)
    waypoint_type = models.CharField(max_length=20, choices=WAYPOINT_TYPE_CHOICES)

    def __str__(self):
        return f"{self.waypoint_type} at {self.location_name} for {self.order}"
