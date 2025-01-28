from rest_framework import serializers
from .models import UserModel


class CustomUserSerializer(serializers.ModelSerializer):
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
            'total_balance'
        ]
        read_only_fields = ['id', 'total_balance',
                            'available_balance','necessary_balance']

    # def validate_role(self, value):
    #     """
    #     Ensure that the role being assigned is valid and allowed.
    #     """
    #     if value not in [UserModel.UserRole.STUDENT, UserModel.UserRole.SPONSOR, UserModel.UserRole.ADMIN]:
    #         raise serializers.ValidationError("Invalid role provided.")
    #     return value

    def create(self, validated_data):
        """
        Custom behavior for creating users.
        For example, you can hash passwords here if the model has a password field.
        """
        return UserModel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Custom behavior for updating user instances.
        Prevent updates to read-only fields like `balance` and `available_balance`.
        """
        for field in self.Meta.read_only_fields:
            validated_data.pop(field, None)  # Remove read-only fields from the update data

        return super().update(instance, validated_data)
