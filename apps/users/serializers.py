from rest_framework import serializers
from apps.utils.serializers import BaseModelSerializer 
from .models import UserModel


class CustomUserSerializer(BaseModelSerializer):
    """
    Serializer for CustomUser model. Handles validation and serialization of user data.
    """
    role = serializers.ChoiceField(choices=UserModel.UserRole.choices)
    class Meta:
        model = UserModel
        fields = [
            'id',
            'first_name',
            'last_name',
            'photo',
            'phone_number',
            'role',
            'degree',
            'university',
            'necessary_balance',
            'available_balance',
            'sponsor_type',
            'total_balance',
	    'created_by',
	    'updated_by'
        ]
        read_only_fields = ['created_by','updated_by','total_balance','available_balance','necessary_balance']

