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

    def validate_phone_number(self, phone_number):
        """ validate phone number """
        return phone_number

    def validate(self, attrs):
        return attrs

    def save(self, **kwargs):
        phone_number = self.validated_data['phone_number']
        auth_code = random.randint(100000, 999999)
        eskiz_uz_service.send_message(phone_number=phone_number, message=f'your auth code is {auth_code}')
        cache.set('phone_number', auth_code, 600 * 10)

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
        print(attrs['auth_code'])
        print(cache.get('phone_number'))
        phone_number = attrs['phone_number']
        auth_code = attrs['auth_code']
        if cache.get('phone_number') != auth_code:
            raise exceptions.ValidationError({"auth_code": "invalid auth code"})

        user, _ = UserModel.objects.get_or_create(phone_number=phone_number)

        refresh = RefreshToken.for_user(user)
        attrs["access_token"] = str(refresh.access_token)
        attrs["refresh_token"] = str(refresh)

        return attrs

# from datetime import timezone, timedelta
#
# from django.contrib.auth import authenticate
# from rest_framework import serializers
# from rest_framework_simplejwt.tokens import RefreshToken
#
#
# class LoginSerializer(serializers.Serializer):
#     phone_number = serializers.CharField(write_only=True)
#     password = serializers.CharField(write_only=True)
#     refresh_token = serializers.CharField(read_only=True)
#     access_token = serializers.CharField(read_only=True)
#
#     def validate(self, attrs):
#         user = authenticate(
#             request=self.context.get('request'),
#             phone_number=attrs.get('phone_number'),
#             password=attrs.get('password')
#         )
#         if user is None:
#             raise serializers.ValidationError("Invalid phone number or password")
#         refresh_token = RefreshToken.for_user(user)
#         refresh_token.payload['phone_number'] = user.phone_number
#         access_token = refresh_token.access_token
#         access_token.set_exp(from_time=timezone.now(),lifetime=timedelta(minutes=60))
#         attrs['refresh'] = str(refresh_token)
#         attrs['access']  = str(access_token)
