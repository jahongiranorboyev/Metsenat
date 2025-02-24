import requests
from django.conf import settings


def send_message(telegram_id, message):
    """
    Telegram foydalanuvchisiga bot orqali xabar yuborish.
    """
    bot_token = settings.TELEGRAM_BOT_TOKEN
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"

    payload = {
        "chat_id": telegram_id,
        "text": message,
        "parse_mode": "HTML"
    }

    response = requests.post(url, json=payload)

    if response.status_code != 200:
        return {"error": response.json()}

    return response.json()
