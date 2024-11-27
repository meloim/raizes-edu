from celery import  shared_task
from django.core.mail import send_mail
from django.conf import settings


@shared_task
def enviar_email_boas_vindas(email_destinarario, nome_usuario):
    assunto = 'Bem-vindo ao sistema'
    mensagem = f"Olá {nome_usuario},\n\nObrigado por se cadastrar em nossa aplicação. Estamos felizes em tê-lo conosco!"
    send_mail(
        assunto,
        mensagem,
        settings.DEFAULT_FROM_EMAIL,
        [email_destinarario],
        fail_silently=False,
        
    )