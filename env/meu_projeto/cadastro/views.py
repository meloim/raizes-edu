from django.shortcuts import render, get_object_or_404, redirect
from .models import Usuario
from .forms import UsuarioForm
import requests



def busca_cep(cep):
    
    cep = ''.join(filter(str.isdigit, cep))

    if len(cep) == 8: 
        url = f'https://viacep.com.br/ws/{cep}/json/'
        response = requests.get(url)

        if response.status_code == 200:
            dados = response.json()

            if 'erro' not in dados:  # Verifica se o CEP não contém erro
                return dados
            else:
                return None  # Se o CEP não for encontrado, retorna None
        else:
            return None  # Se a requisição falhar, retorna None
    else:
        return None  # Caso o CEP não tenha 8 dígitos

    

def base(request):
    return render(request, 'cadastro/base.html')


def listar_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'cadastro/listar_usuarios.html',{'usuarios': usuarios})

def criar_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            cep = form.cleaned_data.get('cep')  
            if cep:
                cep = ''.join(filter(str.isdigit, cep))
                if len(cep) == 8:
                    dados_cep = busca_cep(cep)
                    if dados_cep:
                        form.instance.uf = dados_cep.get('uf', '')
                        form.instance.bairro = dados_cep.get('bairro', '')
                        form.instance.rua = dados_cep.get('logradouro', '')
                        form.instance.complemento = dados_cep.get('complemento', '')
                    else:
                        form.add_error('cep', 'CEP não encontrado.')
            
            form.save()
            return redirect('listar_usuario')
    else:
        form = UsuarioForm()
    return render(request, 'cadastro/criar_usuario.html', {'form': form})


def editar_usuario(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('listar_usuario')
        else:
            form = UsuarioForm(instance=usuario)
            return render(request, 'cadastro/editar_usuario.html',{'form': form})
        
        
def excluir_usuario(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    usuario.delete()
    return redirect('listar_usuario')
        
        
        

