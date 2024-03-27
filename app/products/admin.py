from django.contrib import admin

from .models import Product, ProductReview, Category


class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'created_date')
    list_filter = ('is_active', 'created_date', 'updated_date')
    search_fields = ('name', 'description')
    readonly_fields = ('created_date', 'updated_date')


admin.site.register(Product, ItemAdmin)
admin.site.register(ProductReview)
admin.site.register(Category)
