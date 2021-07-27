import dramatiq
from .send_notification import send_change_status_message


@dramatiq.actor
def send_user_message(message):
    send_change_status_message(message)
