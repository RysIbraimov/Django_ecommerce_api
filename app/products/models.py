from django.db import models

PRODUCT_GRADE_CHOICES = (
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5')
)


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименование", unique=True)
    description = models.TextField(null=True, blank=True, verbose_name="Описание")

    class Meta:
        app_label = 'products'
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименование")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")
    description = models.TextField(null=True, blank=True, verbose_name="Описание")
    quantity = models.IntegerField(blank=True, null=True, verbose_name="Количество")
    is_active = models.BooleanField(default=True, verbose_name="Доступность")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_date = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")

    class Meta:
        app_label = 'products'
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return self.name


class ProductReview(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Товар")
    username = models.CharField(max_length=30, verbose_name="Имя")
    text = models.TextField(verbose_name="Текст")
    mark = models.PositiveSmallIntegerField(choices=PRODUCT_GRADE_CHOICES,
                                            null=True, blank=True, verbose_name="Оценка")

    class Meta:
        app_label = 'products'
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

    def __str__(self):
        return self.username
