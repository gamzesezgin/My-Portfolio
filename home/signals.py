from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from .models import Mail

@receiver(post_save, sender=Mail)
def send_mail_to_admin(sender, instance, created, **kwargs):
    if created:
        subject = "Yeni İletişim Formu Mesajı"
        message = f"Yeni bir iletişim formu mesajı geldi:\n\nE-posta: {instance.mail}\n Mesaj: {instance.message}"
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = [settings.ADMIN_EMAIL]
        send_mail(subject, message, from_email, recipient_list )