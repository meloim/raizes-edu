from django.shortcuts import render, get_object_or_404, redirect
from .models import Usuario
from .forms import UsuarioForm


def homelider(request):
    return render(request, 'home.html')

def base(request):
    return render(request, 'cadastro/base.html')


def listar_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'cadastro/listar_usuarios.html',{'usuarios': usuarios})

def criar_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        print(form)
        if form.is_valid():
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
        
        
        

