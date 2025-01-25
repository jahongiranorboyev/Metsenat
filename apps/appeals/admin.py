from django.contrib import admin
from .models import Appeal


class AppealAdmin(admin.ModelAdmin):
    list_display = ('sponsor', 'phone_number', 'amount', 'available_balance', 'status', 'payment_method')
    list_filter = ('status', 'sponsor')
    search_fields = ('phone_number',)
    readonly_fields = ('available_balance',)


admin.site.register(Appeal, AppealAdmin)
