from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.listar_usuarios, name='listar_usuarios'),
    path('novo/', views.novo_usuario, name='novo_usuario'),
    path('editar/<int:pk>/', views.editar_usuario, name='editar_usuario'),
    path('excluir/<int:pk>/', views.excluir_usuario, name='excluir_usuario'),
]


