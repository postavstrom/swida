# orders/urls.py

from django.urls import path
from .views import OrderListView, OrderCreateView, OrderDetailView, WaypointCreateView, OrderUpdateView, OrderDeleteView

urlpatterns = [
    path('orders/', OrderListView.as_view(), name='order-list'),
    path('orders/create/', OrderCreateView.as_view(), name='order-create'),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
    path('orders/<int:pk>/edit/', OrderUpdateView.as_view(), name='order-update'),
    path('orders/<int:order_id>/waypoints/', WaypointCreateView.as_view(), name='waypoint-create'),
    path('orders/<int:pk>/delete/', OrderDeleteView.as_view(), name='order-delete'),
]
