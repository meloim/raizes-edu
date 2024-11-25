from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    cpf = models.CharField(max_length=12)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=20)
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
    
    
