from django.urls import path, include
from rest_framework import routers

from . import views

order_router = routers.DefaultRouter()
order_router.register(r'orders', views.OrderViewSet, basename='orders')

urlpatterns = [
    path('', include(order_router.urls)),
    path('cart/', views.cart_detail, name='cart_detail'),
    path('cart/add/<int:product_id>/', views.cart_add, name='cart_add'),
    path('cart/remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
    path('cart/get_total_sum/', views.cart_total_sum, name='get_total_sum'),
    path('cart/get_count/', views.cart_count, name='get_count'),
    path('cart/clear/', views.cart_clear, name='clear'),
]

