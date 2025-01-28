from django.contrib import admin

from .models import PaymentMethod, University


@admin.register(PaymentMethod)
class PaymentMethodAdmin(admin.ModelAdmin):
    """
    Admin configuration for the PaymentMethod model.
    """
    list_display = ('name', 'slug', 'created_at', 'updated_at')
    search_fields = ('name',)
    ordering = ('name',)
    readonly_fields = ('created_at', 'updated_at','slug')

@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):
    """
    Admin configuration for the University model.
    """
    list_display = ('name', 'contract_amount', 'created_at', 'updated_at')
    search_fields = ('name',)
    ordering = ('name',)
    readonly_fields = ('created_at', 'updated_at','slug')



