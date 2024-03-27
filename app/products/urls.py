from django.urls import include, path
from rest_framework import routers

from . import views

products_router = routers.DefaultRouter()
products_router.register(r'products', views.ProductViewSet, basename='product')
products_router.register(r'reviews', views.ProductReviewViewSet, basename='product-review')
products_router.register(r'categories', views.CategoryViewSet, basename='category')


urlpatterns = [
    path('', include(products_router.urls)),
]