from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser

class CustomUserAdmin(BaseUserAdmin):
    # Configuration for the user list page
    list_display = ('phone_number', 'first_name', 'last_name', 'role', 'is_active')
    list_filter = ('role', 'is_active', 'is_staff', 'is_superuser')
    search_fields = ('phone_number', 'first_name', 'last_name')
    ordering = ('phone_number',)

    # Configuration for user creation or editing page
    fieldsets = (
        (None, {'fields': ('phone_number', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'photo', 'email', 'university', 'degree', 'sponsor_type')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
        ('Additional info', {'fields': ('role', )}),
    )

    # Configuration for the Add New User page
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone_number', 'first_name', 'last_name', 'role','university', 'degree', 'sponsor_type'),
        }),
    )

        # Override default methods to avoid password prompts
    def get_fieldsets(self, request, obj=None):
        if not obj:
            return self.add_fieldsets
        return super().get_fieldsets(request, obj)

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ('password',)
        return ()

admin.site.register(CustomUser, CustomUserAdmin)
