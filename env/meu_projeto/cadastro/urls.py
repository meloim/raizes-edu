from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('lista/', views.listar_usuarios, name='listar_usuarios'),
    path('novo/', views.criar_usuario, name='criar_usuario'),
    path('editar/<int:pk>/', views.editar_usuario, name='editar_usuario'),
    path('excluir/<int:pk>/', views.excluir_usuario, name='excluir_usuario'),
    path('home/',views.homelider, name='home_lider'),

    
   
]
   
   



