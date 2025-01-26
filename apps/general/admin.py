from django.contrib import admin

from .models import PaymentMethod, University


@admin.register(PaymentMethod)
class PaymentMethodAdmin(admin.ModelAdmin):
    """
    Admin configuration for the PaymentMethod model.
    """
    list_display = ('name', 'slug', 'created_at', 'updated_at')  # Fields to display in the admin list view
    search_fields = ('name', 'slug')  # Fields to search
    prepopulated_fields = {'slug': ('name',)}  # Automatically generate slug based on the name
    ordering = ('name',)  # Default ordering
    readonly_fields = ('created_at', 'updated_at')  # Fields that are read-only in the admin panel


@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):
    """
    Admin configuration for the University model.
    """
    list_display = ('name', 'contract_amount', 'slug', 'created_at', 'updated_at')  # Fields to display
    search_fields = ('name', 'slug')  # Searchable fields
    ordering = ('name',)  # Default ordering
    readonly_fields = ('slug', 'created_at', 'updated_at')  # Fields that are read-only
    fieldsets = (
        (None, {
            'fields': ('name', 'contract_amount')  # Grouping fields for better admin layout
        }),
        ('Slug and Metadata', {
            'fields': ('slug', 'created_at', 'updated_at'),
        }),
    )

