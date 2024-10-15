from rest_framework import generics
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView

from rest_framework import status
from .models import Order, Waypoint
from .serializers import OrderSerializer, WaypointSerializer

class OrderListView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderDetailView(RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderCreateView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class WaypointCreateView(generics.CreateAPIView):
    queryset = Waypoint.objects.all()
    serializer_class = WaypointSerializer

    def perform_create(self, serializer):
        order_id = self.kwargs.get('order_id')
        order = Order.objects.get(id=order_id)
        serializer.save(order=order)

class OrderUpdateView(generics.UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderDeleteView(generics.DestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
