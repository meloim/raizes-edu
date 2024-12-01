from django.db import models
from django.contrib.auth.hashers import make_password


class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    cpf = models.CharField(max_length=12)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=128)  # Aumente o tamanho para acomodar o hash
    cep = models.CharField(max_length=12)
    uf = models.CharField(max_length=20)
    bairro = models.CharField(max_length=20)
    rua = models.CharField(max_length=100)
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=100, blank=True, null=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    tipoUsuario = models.CharField(max_length=20)
    
    
    def __str__(self):
        return self.nome
    
    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super().save(*args, **kwargs)
    
