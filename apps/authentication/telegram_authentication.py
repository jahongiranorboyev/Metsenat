import hashlib
import hmac
import time
from django.conf import settings

class TelegramAuthentication:
    @staticmethod
    def verify_telegram_auth(data):
        """Telegram login ma’lumotlarini tekshirish"""
        auth_data = data.copy()
        auth_data.pop('hash', None)

        check_string = "\n".join(f"{k}={v}" for k, v in sorted(auth_data.items()))
        secret_key = hashlib.sha256(settings.TELEGRAM_BOT_TOKEN.encode()).digest()
        calculated_hash = hmac.new(secret_key, check_string.encode(), hashlib.sha256).hexdigest()

        return calculated_hash == data.get('hash') and int(data.get('auth_date', 0)) > time.time() - 86400
