from __future__ import absolute_import, unicode_literals
import os
from celery import Celery


#Definindo o módulo do Celery a ser usado
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cadastro.settings')

app = Celery('cadastro')


#usando a string aqui faz com que o Celery use o sistema de configuração do Django
app.config_from_object('django.conf:settings', namespace='CELERY')

#Carregar automaticamente a tarefas de todos os aplicativos registros no Django
app.autodiscover_tasks