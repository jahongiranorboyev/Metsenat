import random

from django.core.cache import cache
from rest_framework import serializers, exceptions

from apps.users.models import UserModel
from apps.utils.functions import uzbek_phone_validator
# from apps.authentication.tests import eskiz_uz_service
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from apps.utils.functions.send_message_tg import send_message


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


class TelegramAuthSerializer(serializers.Serializer):
    id = serializers.CharField()
    username = serializers.CharField(required=False, allow_blank=True)
    first_name = serializers.CharField(required=False, allow_blank=True)
    auth_date = serializers.IntegerField(write_only=True)
    hash = serializers.CharField(write_only=True)

    def validate(self, data):
        """
        Telegram login uchun hashni tekshirish
        """
        import hashlib
        import hmac
        import time
        from django.conf import settings

        bot_token = settings.TELEGRAM_BOT_TOKEN
        auth_date = data.get("auth_date", 0)

        # ✅ Eskirgan ma’lumotlarni rad etish (5 daqiqadan oshsa)
        if time.time() - auth_date > 300:
            raise serializers.ValidationError("Telegram login expired")

        # ✅ Hashni tekshirish
        data_check_string = "\n".join(
            [f"{k}={data[k]}" for k in sorted(data.keys()) if k != "hash"]
        )
        secret_key = hashlib.sha256(bot_token.encode()).digest()
        expected_hash = hmac.new(secret_key, data_check_string.encode(), hashlib.sha256).hexdigest()

        if expected_hash != data.get("hash"):
            raise serializers.ValidationError("Invalid Telegram login")

        return data

    def create_or_update_user(self, validated_data):
        """
        Foydalanuvchini yaratish yoki yangilash va JWT token qaytarish
        """
        telegram_id = validated_data["id"]
        username = validated_data.get("username", f"user_{telegram_id}")

        user, created = UserModel.objects.get_or_create(
            telegram_id=telegram_id,
            defaults={
                "full_name": username,
                "phone_number": f"+998000000{telegram_id % 10000}",
                "role": UserModel.UserRole.SPONSOR
            }
        )

        # ✅ JWT token yaratish
        refresh = RefreshToken.for_user(user)

        # ✅ Telegramga xabar yuborish
        message = (
            "✅ <b>Salom!</b> Siz tizimga muvaffaqiyatli kirdingiz.\n\n"
            "🔹 <b>Sayt:</b> metsenat.john-tuit-dev.uz\n"
            f"🔹 <b>Foydalanuvchi:</b> @{username}"
        )
        send_message(telegram_id, message)

        return {
            "access": str(refresh.access_token),
            "refresh": str(refresh),
            "user": {
                "id": user.id,
                "username": user.username
            }
        }
