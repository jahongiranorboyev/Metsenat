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

