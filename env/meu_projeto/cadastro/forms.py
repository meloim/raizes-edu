from django import forms
from .models import Usuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = [ 'nome', 'data_nascimento', 'cpf', 'email', 'password', 'cep', 'uf', 'bairro', 'rua', 'numero',
                  'complemento', 'telefone','tipoUsuario']
        widgets = {
            'data_nascimento': forms.DateInput(attrs ={'type': 'date'}),
            'password': forms.PasswordInput(),
        }
        
class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
        
