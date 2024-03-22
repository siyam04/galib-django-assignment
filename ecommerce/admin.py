from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser


# Group will not show in admin panel
admin.site.unregister(Group)


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
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

    ordering = ('-id',)
