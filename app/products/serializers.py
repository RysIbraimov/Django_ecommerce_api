from rest_framework import serializers

from .models import Product, Category, ProductReview


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = "__all__"


class ProductReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductReview
        fields = "__all__"
