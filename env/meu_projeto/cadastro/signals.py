from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .task import enviar_email_boas_vindas
from .models import Usuario


@receiver(post_save, sender=Usuario)
def enviar_email_ao_cadastrar(sender, instance, created, **kwargs):
    if created:
        # Chama a tarefa Celery para enviar op e-mail de boas-vindas
        enviar_email_boas_vindas.apply_async(args=[instance.email, instance.nome])