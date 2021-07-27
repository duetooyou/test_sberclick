from django.conf import settings
import telegram

URL = settings.BOT_URL
my_token = settings.BOT_TOKEN
my_chat_id = settings.BOT_CHAT_ID


def send_change_status_message(notification_message):
    my_bot = telegram.Bot(my_token)
    my_bot.send_message(my_chat_id, message=notification_message)
