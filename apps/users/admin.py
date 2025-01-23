from django.contrib import admin
from .models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    model = CustomUser
    ordering = ['phone_number']  # phone_number bo'yicha tartiblang

admin.site.register(CustomUser, CustomUserAdmin)  # CustomUser modelini ro'yxatga olish
