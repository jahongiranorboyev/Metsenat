from rest_framework import serializers
from .models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            'id', 'username', 'first_name',
            'last_name', 'email', 'phone_number',
            'photo', 'balance', 'university', 'degree'
        ]


class SponsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            'id', 'username', 'first_name',
            'last_name', 'email', 'phone_number',
            'photo', 'balance', 'university', 'degree'
        ]
