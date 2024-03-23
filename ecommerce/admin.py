from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin

from .models import *


# Group will not show in admin panel
admin.site.unregister(Group)


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    """
    Custom admin class for viewing & adding new user with user_type field
    """
    fieldsets = (
        (None, {'fields': ('username', 'password', 'user_type')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'first_name', 'last_name', 'email', 'user_type', 'password1', 'password2'),
        }),
    )

    list_display = (
        'id', 'username', 'first_name', 'last_name', 'email',
        'user_type', 'is_active', 'is_staff', 'is_superuser'
    )

    list_editable = ('user_type', 'is_active', 'is_staff', 'is_superuser')
    list_display_links = ['username']
    ordering = ('-id',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'seller', 'description']
    list_display_links = ['name']
    ordering = ['-id']


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['id', 'user']
    list_display_links = ['user']
    ordering = ['-id']


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'cart', 'product', 'quantity']
    list_display_links = ['product']
    ordering = ['-id']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'total_amount', 'date_ordered']
    list_display_links = ['user']
    ordering = ['-id']


@admin.register(DailyData)
class DailyDataAdmin(admin.ModelAdmin):
    list_display = ['id', 'date', 'revenue']
    list_display_links = ['date']
    ordering = ['-id']
