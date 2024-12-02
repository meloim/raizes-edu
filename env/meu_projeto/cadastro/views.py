from django.shortcuts import render, get_object_or_404, redirect
from .models import Usuario
from django.http import JsonResponse
from .forms import UsuarioForm, LoginForm
from django.contrib.auth.hashers import check_password
from .error_handling import handle_login_error, handle_login_success

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
                    # Retorna a mensagem de sucesso como JSON
                    return JsonResponse(handle_login_success())
                else:
                    error_message = 'Email ou senha incorretos'
            except Usuario.DoesNotExist:
                error_message = 'Email ou senha incorretos'
            
            # Retorna o erro como JSON
            return JsonResponse(handle_login_error(error_message))
    else:
        form = LoginForm()
    return render(request, 'cadastro/login.html', {'form': form})

def homelider(request):
    usuario_id = request.session.get('usuario_id')
    if not usuario_id:
        return redirect('login')
    usuario = get_object_or_404(Usuario, id=usuario_id)
    return render(request, 'cadastro/homelider.html', {'usuario': usuario})
        

def criar_turmas(request):
    return render(request, 'cadastro/criar_turmas.html')

        
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