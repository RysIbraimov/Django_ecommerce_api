from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'name', 'is_staff')
    search_fields = ('username', 'email', 'name')
    ordering = ('username',)


admin.site.register(CustomUser, CustomUserAdmin)
