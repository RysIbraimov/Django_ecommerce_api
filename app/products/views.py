from rest_framework import viewsets, mixins
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import Product, ProductReview, Category
from .serializers import ProductSerializer, ProductReviewSerializer, CategorySerializer


class PostPagePagination(PageNumberPagination):
    page_size = 10


class CategoryViewSet(viewsets.ModelViewSet):
    """
    API для создания и получения категорий товаров
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = PostPagePagination


class ProductViewSet(viewsets.ModelViewSet):
    """
    API для получения списка товаров
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['name', 'category', 'is_active']
    search_fields = ['name', 'description']
    ordering_fields = ['name', 'created_date', 'price']
    pagination_class = PostPagePagination


class ProductReviewViewSet(viewsets.ModelViewSet):
    """
    API для создания и получения отзывов
    """
    queryset = ProductReview.objects.all()
    serializer_class = ProductReviewSerializer
    pagination_class = PostPagePagination
