from django import forms
from .models import Usuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = [ 'nome', 'data_nascimento', 'cpf', 'email', 'password', 'cep', 'uf', 'bairro', 'rua', 'numero',
                  'complemento', 'telefone','tipoUsuario']