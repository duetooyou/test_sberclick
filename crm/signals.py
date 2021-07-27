from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from .models import Claim, Client
from .send_notification import send_change_status_message


@receiver(pre_save, sender=Claim)
def send_message(sender, instance, created=False, **kwargs):
    message_for_user = f"По вашей заявке № {instance.id} изменился статус." \
                       f" Статус вашей заявки: {instance.status}"
    if Claim.objects.filter(pk=instance.id).exists() and Claim.objects.get(id=instance.id).owner.notification and \
            instance.status != Claim.objects.get(pk=instance.id).status:
        print(Claim.objects.get(id=instance.id).owner.notification)
        send_change_status_message(message_for_user)


@receiver(post_save, sender=Claim)
def send_message(sender, instance, created, **kwargs):
    message_for_user = f"{instance.owner} Ваша заявка создана № {instance.id}" \
                       f" Статус вашей заявки: {instance.status}"
    if created and Claim.objects.get(id=instance.id).owner.notification:
        send_change_status_message(message_for_user)
