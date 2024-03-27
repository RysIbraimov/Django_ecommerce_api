from rest_framework import serializers
from .models import Order

class CartSerializer(serializers.Serializer):
    quantity = serializers.IntegerField()
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    product = serializers.CharField()
    product_id = serializers.IntegerField()
    total_price = serializers.DecimalField(max_digits=10, decimal_places=2)


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'

    def validate(self, data):
        if not data['first_name'].isalpha():
            raise serializers.ValidationError('Недопустимые символы!')
        if not data['last_name'].isalpha():
            raise serializers.ValidationError('Недопустимые символы!')
        return data
