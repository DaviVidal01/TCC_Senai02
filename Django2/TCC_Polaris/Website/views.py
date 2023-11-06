from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from Website.forms import FotoForms, LoginForms, RegisterForms
from .models import Comentarios_BD, Fotos_BD, Like_BD
from django.contrib.auth.forms import UserCreationForm

# -----> USER PAGE
def index(request):
    likes_view = Like_BD.objects.all()
    fotos_view = Fotos_BD.objects.all()
    comentarios_view = Comentarios_BD.objects.all()
    user_form = LoginForms()
    user = User.objects.all()
    return render(request, 'index.html', {'user':user, 'user_form': user_form ,'likes': likes_view,'fotos': fotos_view,'comentarios': comentarios_view})

def detalhes_fotos(request):
    likes_view = Like_BD.objects.all()
    fotos_view = Fotos_BD.objects.all()
    comentarios_view = Comentarios_BD.objects.all()
    user = User.objects.all()
    return render(request, 'detalhes_fotos.html', {'likes': likes_view,'fotos': fotos_view,'comentarios': comentarios_view})

# -----> DASHBOARD ADMIN PAGE

def dashboard(request):
    user = User.objects.all()
    likes_view = Like_BD.objects.all()
    fotos_view = Fotos_BD.objects.all()
    comentarios_view = Comentarios_BD.objects.all()
    return render(request, 'dashboard.html', {'user':user, 'likes': likes_view,'fotos': fotos_view,'comentarios': comentarios_view})

def consulta_fotos(request):
    user = User.objects.all()
    likes_view = Like_BD.objects.all()
    fotos_view = Fotos_BD.objects.all()
    comentarios_view = Comentarios_BD.objects.all()
    return render(request, 'dashboardC.html', {'user':user, 'likes': likes_view,'fotos': fotos_view,'comentarios': comentarios_view})

def add_fotos(request):
    if request.method == 'POST':
        foto_form = FotoForms(request.POST, request.FILES)
        if foto_form.is_valid():
            foto = foto_form.save(commit=False)
            foto.autor = request.user
            foto.save()
            return redirect('add_fotos')
    else:
        foto_form = FotoForms()

    return render(request, 'dashboardA.html', {'foto_form': foto_form})


# -----> LOGIN LOGOUT AUTH
def login_user(request):
    user_form = LoginForms()

    if request.method == 'POST':
        user_form = LoginForms(request.POST)

        if user_form.is_valid():
            email = user_form.cleaned_data['email']
            senha = user_form.cleaned_data['senha']
            user = authenticate(request, username=email, password=senha)

            if user is not None:
                auth_login(request, user)
                messages.success(request, 'Foi logado com sucesso!')

                if user.is_staff:
                    return redirect('dashboard')
                else:
                    return redirect('index')
            else:
                messages.error(request, 'Erro ao efetuar login')
                return redirect('index')

    return render(request, 'index.html', {'user_form': user_form})

def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Usuário cadastrado com sucesso!')
            return redirect('index')
    else:
        form = UserCreationForm()
    
    return render(request, 'index.html', {'register_form': form})

@login_required
def logout_user(request):
    auth.logout(request)
    messages.success(request, 'Logout efetuado com sucesso!')
    return redirect('index')

@login_required
def inative(request, id):
    user = User.objects.get(id=id)
    user.is_active = False
    user.save()
    messages.success(request, 'Usuario inativado com sucesso!')
    return redirect('users')

@login_required
def active(request, id):
    user = User.objects.get(id=id)
    user.is_active = True
    user.save()
    messages.success(request, 'Usuario ativado com sucesso!')
    return redirect('users')