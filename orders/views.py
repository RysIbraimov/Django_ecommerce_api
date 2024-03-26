from django.shortcuts import redirect, get_object_or_404

from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.models import Product
from .models import OrderItem, Order
from .cart import Cart

from .serializers import CartSerializer, OrderSerializer


class OrderViewSet(viewsets.ModelViewSet):
    """
    API для создания заказов
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):
        cart = Cart(request)
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            order = serializer.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity']
                )
            cart.clear()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def order_paid(request, order_id):
    """
    Изменение статуса оплаты заказа по ID.
    """
    order = get_object_or_404(Order, id=order_id)
    if order.paid:
        return Response("Заказ уже оплачен!")
    else:
        order.paid = True
        order.save()
        return Response("Оплата принята!")


@api_view(['GET'])
def order_delivery(request, order_id):
    """
    Изменение статуса доставки заказа по ID.
    """
    order = get_object_or_404(Order, id=order_id)
    if order.delivery:
        order.paid = False
        order.save()
        return Response("Статус изменен на самовывоз")
    else:
        return Response("Статус уже самовывоз!")


@api_view(['POST'])
def cart_add(request, product_id):
    """
    Добавление товара в корзину по ID.
    """
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    quantity = request.data.get('quantity', 1)
    cart.add(product=product, quantity=quantity)
    return redirect('cart_detail')


@api_view(['GET'])
def cart_remove(request, product_id):
    """
    Удаление товара из корзины по ID.
    """
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart_detail')


@api_view(['GET'])
def cart_clear(request):
    """
    Очистка корзины.
    """
    cart = Cart(request)
    cart.clear()
    return redirect('cart_detail')


@api_view(['GET'])
def cart_total_sum(request):
    """
    Получение полной стоимости всех товаров.
    """
    cart = Cart(request)
    return Response(cart.get_total_price())


@api_view(['GET'])
def cart_count(request):
    """
    Получение количества всех товаров.
    """
    cart = Cart(request)
    return Response(len(cart))


@api_view(['GET'])
def cart_detail(request):
    """
    Получение списка всех товаров в корзине.
    """
    cart = Cart(request)
    serializer = CartSerializer(cart, many=True)
    return Response(serializer.data)
