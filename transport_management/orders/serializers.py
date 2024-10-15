# orders/serializers.py

from rest_framework import serializers
from .models import Order, Waypoint

class WaypointSerializer(serializers.ModelSerializer):
    class Meta:
        model = Waypoint
        fields = ['id', 'location_name', 'waypoint_type', 'order']
        read_only_fields = ['order']

class OrderSerializer(serializers.ModelSerializer):
    waypoints = WaypointSerializer(many=True, required=False)

    class Meta:
        model = Order
        fields = ['id', 'order_number', 'customer_name', 'date', 'waypoints']

    def update(self, instance, validated_data):
        # Získame dáta o waypointoch z requestu
        waypoints_data = validated_data.pop('waypoints', [])

        # Najprv aktualizujeme objednávku samotnú
        instance.order_number = validated_data.get('order_number', instance.order_number)
        instance.customer_name = validated_data.get('customer_name', instance.customer_name)
        instance.date = validated_data.get('date', instance.date)
        instance.save()

        # Prepracujeme waypointy
        existing_waypoints = {waypoint.id: waypoint for waypoint in instance.waypoints.all()}

        # Iterujeme cez waypointy poslané z FE
        for waypoint_data in waypoints_data:
            waypoint_id = waypoint_data.get('id')
            if waypoint_id and waypoint_id in existing_waypoints:
                # Ak waypoint už existuje, aktualizujeme ho
                waypoint = existing_waypoints.pop(waypoint_id)
                waypoint.location_name = waypoint_data.get('location_name', waypoint.location_name)
                waypoint.waypoint_type = waypoint_data.get('waypoint_type', waypoint.waypoint_type)
                waypoint.save()
            else:
                # Ak waypoint neexistuje, vytvoríme nový a priradíme ho k objednávke
                Waypoint.objects.create(order=instance, **waypoint_data)

        # Zvyšné waypointy, ktoré neboli poslané v requeste, zmažeme
        for waypoint in existing_waypoints.values():
            waypoint.delete()

        return instance
