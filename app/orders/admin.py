from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ('product', )


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'address', 'created_date')
    list_filter = ('paid', 'created_date', 'updated_date')
    inlines = [OrderItemInline]
    search_fields = ('address', 'city', 'first_name', 'last_name')


admin.site.register(Order, OrderAdmin)