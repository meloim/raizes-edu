from django.shortcuts import render, get_object_or_404, redirect
from .models import Usuario
from .forms import UsuarioForm, LoginForm
from django.contrib.auth.hashers import check_password

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                usuario = Usuario.objects.get(email=email)
                if check_password(password, usuario.password):
                    request.session['usuario_id'] = usuario.id
                    return redirect('homelider')
                else:
                    form.add_error(None, 'Email ou senha incorretos')
            except Usuario.DoesNotExist:
                form.add_error(None, 'Email ou senha incorretos')
    else:
        form = LoginForm()
    return render(request, 'cadastro/login.html', {'form': form})

def homelider(request):
    usuario_id = request.session.get('usuario_id')
    if not usuario_id:
        return redirect('login')
    usuario = get_object_or_404(Usuario, id=usuario_id)
    return render(request, 'cadastro/homelider.html', {'usuario': usuario})
        



        
def base(request):
    return render(request, 'cadastro/base.html')

def listar_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'cadastro/listar_usuarios.html', {'usuarios': usuarios})

def criar_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
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
            return render(request, 'cadastro/editar_usuario.html', {'form': form})
        
def excluir_usuario(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    usuario.delete()
    return redirect('listar_usuario')