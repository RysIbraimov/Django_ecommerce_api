from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from orders.models import Order
from products.models import Product, Category


class OrderViewSetTestCase(APITestCase):
    def setUp(self):
        self.order_data = {
            "first_name": "John",
            "last_name": "Doe",
            "email": "johndoe@example.com",
            "phone": "1234567890",
            "address": "123 Main St",
            "city": "Anytown"
        }

    def test_create_order(self):
        url = reverse('orders-list')
        response = self.client.post(url, self.order_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Order.objects.count(), 1)
        self.assertEqual(Order.objects.last().first_name, "John")

    def test_list_orders(self):
        url = reverse('orders-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_order(self):
        order = Order.objects.create(**self.order_data)
        url = reverse('orders-detail', args=[order.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class OrderPaidViewTestCase(APITestCase):
    def setUp(self):
        self.order = Order.objects.create(
            first_name="John",
            last_name="Doe",
            email="johndoe@example.com",
            phone="1234567890",
            address="123 Main St",
            city="Anytown",
            paid=False  # Initially not paid
        )
        self.url = reverse('order_paid', kwargs={'order_id': self.order.id})


    def test_order_paid(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.order.refresh_from_db()
        self.assertTrue(self.order.paid)


class CartAddViewTestCase(APITestCase):
    def setUp(self):
        self.category1 = Category.objects.create(name="Category 1", description="Description 1")
        self.product = Product.objects.create(
            name="Product 1", price=10.99, category=self.category1, quantity=2, is_active=True)
        self.data = {'quantity': 2}

    def test_cart_add(self):
        url = reverse('cart_add', kwargs={'product_id': self.product.id})
        response = self.client.post(url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)

    def test_cart_remove(self):
        url = reverse('cart_remove', kwargs={'product_id': self.product.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)

    def test_cart_clear(self):
        response = self.client.get(reverse('cart_clear'))
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)

    def test_cart_total_sum(self):
        response = self.client.get(reverse('get_total_sum'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cart_count(self):
        response = self.client.get(reverse('get_cart_count'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)






