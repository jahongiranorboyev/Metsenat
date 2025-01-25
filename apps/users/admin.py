from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    """
    Custom admin panel configuration for CustomUser model.
    """
    model = CustomUser
    list_display = (
        'id',
        'phone_number',
        'first_name',
        'last_name',
        'role',
        'balance',
        'available_balance',
        'university',
        'sponsor_type',
        'is_active',
        'is_staff',
    )
    list_filter = (
        'role',
        'degree',
        'university',
        'sponsor_type',
        'is_active',
        'is_staff',
        'is_superuser',
    )
    search_fields = ('phone_number', 'first_name', 'last_name')
    ordering = ('id',)
    fieldsets = (
        (None, {
            'fields': (
                'phone_number',
                'password',
                'first_name',
                'last_name',
                'photo',
                'role',
                'degree',
                'balance',
                'available_balance',
                'university',
                'sponsor_type',
            )
        }),
        ('Permissions', {
            'fields': (
                'is_active',
                'is_staff',
                'is_superuser',
                'groups',
                'user_permissions',
            )
        }),
        ('Important Dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'phone_number',
                'password1',
                'password2',
                'first_name',
                'last_name',
                'role',
                'degree',
                'university',
                'sponsor_type',
                'is_active',
                'is_staff',
            )
        }),
    )

