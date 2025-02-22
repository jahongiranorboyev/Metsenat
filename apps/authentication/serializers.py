import random

from django.core.cache import cache
from rest_framework import serializers, exceptions
from rest_framework_simplejwt.tokens import RefreshToken

from apps.users.models import UserModel
from apps.utils.functions import uzbek_phone_validator
from apps.authentication.tests import eskiz_uz_service


class SendAuthCodeSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=13,
                                         min_length=13,
                                         required=True,
                                         allow_null=False,
                                         validators=[uzbek_phone_validator],
                                         write_only=True)

    def save(self, **kwargs):
        phone_number = self.validated_data['phone_number']
        auth_code = random.randint(100000, 999999)
        #        eskiz_uz_service.send_message(phone_number=phone_number, message=f'your auth code is {auth_code}')
        cache.set('phone_number', auth_code, 10 * 60)


print(cache.get('phone_number'))


class AuthCodeConfirmSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=13,
                                         min_length=13,
                                         required=True,
                                         allow_null=False,
                                         validators=[uzbek_phone_validator],
                                         write_only=True)

    auth_code = serializers.IntegerField(write_only=True)
    access_token = serializers.CharField(read_only=True)
    refresh_token = serializers.CharField(read_only=True)

    def validate(self, attrs):
        auth_code = attrs['auth_code']
        phone_number = attrs['phone_number']
        if cache.get('phone_number') != auth_code:
            raise exceptions.ValidationError({"auth_code": "invalid auth code"})

        user, _ = UserModel.objects.get_or_create(
            phone_number=phone_number,
            defaults={'role': UserModel.UserRole.SPONSOR}
        )

        refresh = RefreshToken.for_user(user)
        attrs["access_token"] = str(refresh.access_token)
        attrs["refresh_token"] = str(refresh)

        cache.delete('phone_number')

        return attrs


class LogoutSerializer(serializers.Serializer):
    refresh_token = serializers.CharField()

    def validate_refresh_token(self, value):
        """ Check token validity """
        from rest_framework_simplejwt.tokens import RefreshToken
        try:
            RefreshToken(value)
        except Exception as e:
            raise serializers.ValidationError("Invalid refresh token.")
        return value
