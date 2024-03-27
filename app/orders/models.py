from django.db import models

from products.models import Product


class Order(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="Имя")
    last_name = models.CharField(max_length=50, verbose_name="Фамилия")
    email = models.EmailField(null=True, blank=True, verbose_name="Почта")
    phone = models.CharField(max_length=20, verbose_name="Номер телефона")
    address = models.CharField(null=True, blank=True, max_length=250, verbose_name="Адрес")
    city = models.CharField(null=True, blank=True, max_length=100, verbose_name="Город")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_date = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")
    paid = models.BooleanField(default=False, verbose_name="Оплачено")

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'Order {self.id}'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL, related_name='order_items')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    quantity = models.PositiveIntegerField(default=1, verbose_name="Количество")

    class Meta:
        verbose_name = 'Товары заказа'
        verbose_name_plural = 'Товары заказа'

    def __str__(self):
        return f'Order {self.pk}'

    def get_cost(self):
        return self.price * self.quantity
