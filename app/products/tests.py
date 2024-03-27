from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from products.models import Product, Category, ProductReview


class CategoryViewSetTestCase(APITestCase):
    def setUp(self):
        self.category1 = Category.objects.create(name="Category 1", description="Description 1")
        self.category2 = Category.objects.create(name="Category 2", description="Description 2")

    def test_list_categories(self):
        url = reverse('category-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_category(self):
        url = reverse('category-detail', args=[self.category1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.category1.name)

    def test_create_category(self):
        url = reverse('category-list')
        data = {
            "name": "New Category",
            "description": "New Description"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Category.objects.count(), 3)
        self.assertEqual(Category.objects.last().name, "New Category")


class ProductViewSetTestCase(APITestCase):
    def setUp(self):
        self.category1 = Category.objects.create(name="Category 1", description="Description 1")
        self.product1 = Product.objects.create(
            name="Product 1", price=10.99, category=self.category1, quantity=2, is_active=True)

    def test_list_products(self):
        url = reverse('product-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_product(self):
        url = reverse('product-detail', args=[self.product1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.product1.name)

    def test_create_product(self):
        url = reverse('product-list')
        data = {
            "name": "New Product",
            "price": 29.99,
            "category": self.category1.id,
            "quantity": 3,
            "is_active": True
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 2)
        self.assertEqual(Product.objects.last().name, "New Product")


class ProductReviewViewSetTestCase(APITestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Category 1", description="Description 1")
        self.product = Product.objects.create(
            name="Product 1", price=10.99, category=self.category, quantity=5, is_active=True)
        self.review1 = ProductReview.objects.create(
            product=self.product, username="User1", text="Review 1", mark=4)
        self.review2 = ProductReview.objects.create(
            product=self.product, username="User2", text="Review 2", mark=3)

    def test_list_reviews(self):
        url = reverse('product-review-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_review(self):
        url = reverse('product-review-detail', args=[self.review1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['text'], self.review1.text)

    def test_create_review(self):
        url = reverse('product-review-list')
        data = {
            "product": self.product.id,
            "username": "NewUser",
            "text": "New Review",
            "mark": 5
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ProductReview.objects.count(), 3)
        self.assertEqual(ProductReview.objects.last().username, "NewUser")