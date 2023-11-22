from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render, get_object_or_404, redirect
from Website.forms import FotoForms, LoginForms, RegisterForms
from .models import Comentarios_BD, Fotos_BD, Like_BD, Barra_Pesquisa
from django.contrib.auth.forms import UserCreationForm

from django.db.models import Q

# -----> USER PAGE
def index(request):
    likes_view = Like_BD.objects.all()
    fotos_view = Fotos_BD.objects.all()
    register_form = RegisterForms()
    login_form = LoginForms()
    imagem_view = Barra_Pesquisa.objects.all()
    comentarios_view = Comentarios_BD.objects.all()
    user = User.objects.all()
    return render(request, 'index.html', {'register_form':register_form,'user_form': login_form ,'likes': likes_view,'fotos': fotos_view,'comentarios': comentarios_view,'imagens': imagem_view})

def faq(request):
    likes_view = Like_BD.objects.all()
    fotos_view = Fotos_BD.objects.all()
    register_form = RegisterForms()
    login_form = LoginForms()
    imagem_view = Barra_Pesquisa.objects.all()
    comentarios_view = Comentarios_BD.objects.all()
    user = User.objects.all()
    return render(request, 'faq.html', {'register_form':register_form,'user_form': login_form ,'likes': likes_view,'fotos': fotos_view,'comentarios': comentarios_view,'imagens': imagem_view})

def dicas(request):
    likes_view = Like_BD.objects.all()
    fotos_view = Fotos_BD.objects.all()
    register_form = RegisterForms()
    login_form = LoginForms()
    imagem_view = Barra_Pesquisa.objects.all()
    comentarios_view = Comentarios_BD.objects.all()
    user = User.objects.all()
    return render(request, 'dicas.html', {'register_form':register_form,'user_form': login_form ,'likes': likes_view,'fotos': fotos_view,'comentarios': comentarios_view,'imagens': imagem_view})

def sobre(request):
    likes_view = Like_BD.objects.all()
    fotos_view = Fotos_BD.objects.all()
    register_form = RegisterForms()
    login_form = LoginForms()
    imagem_view = Barra_Pesquisa.objects.all()
    comentarios_view = Comentarios_BD.objects.all()
    user = User.objects.all()
    return render(request, 'sobre.html', {'register_form':register_form,'user_form': login_form ,'likes': likes_view,'fotos': fotos_view,'comentarios': comentarios_view,'imagens': imagem_view})

def catalogo(request):
    likes_view = Like_BD.objects.all()
    fotos_view = Fotos_BD.objects.all()
    register_form = RegisterForms()
    login_form = LoginForms()
    imagem_view = Barra_Pesquisa.objects.all()
    comentarios_view = Comentarios_BD.objects.all()
    user = User.objects.all()
    return render(request, 'catalogo.html', {'register_form':register_form,'user_form': login_form ,'likes': likes_view,'fotos': fotos_view,'comentarios': comentarios_view,'imagens': imagem_view})

# -----> DASHBOARD ADMIN PAGE

@login_required
def dashboard(request):
    user = User.objects.all()
    likes_view = Like_BD.objects.all()
    fotos_view = Fotos_BD.objects.all()
    comentarios_view = Comentarios_BD.objects.all()
    return render(request, 'dashboard.html', {'user':user, 'likes': likes_view,'fotos': fotos_view,'comentarios': comentarios_view})

@login_required
def consulta_fotos(request):
    user = User.objects.all()
    likes_view = Like_BD.objects.all()
    fotos_view = Fotos_BD.objects.all()
    comentarios_view = Comentarios_BD.objects.all()
    return render(request, 'dashboardConsulta_fotos.html', {'user':user, 'likes': likes_view,'fotos': fotos_view,'comentarios': comentarios_view})

@login_required
def consulta_users(request):
    user = User.objects.all()
    likes_view = Like_BD.objects.all()
    fotos_view = Fotos_BD.objects.all()
    comentarios_view = Comentarios_BD.objects.all()
    return render(request, 'dashboardConsulta_user.html', {'user':user, 'likes': likes_view,'fotos': fotos_view,'comentarios': comentarios_view})

@login_required
def add_user(request):
    if request.method == 'POST':
        register_form = RegisterForms(request.POST)
        if register_form.is_valid():
            user = register_form.save(commit=False)
            user.save()
            return redirect('add_user')
    else:
        register_form = RegisterForms()

    return render(request, 'dashboardAdd_user.html', {'register_form': register_form})

@login_required
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

    return render(request, 'dashboardAdd_fotos.html', {'foto_form': foto_form})

# -----> Like ADD
def add_like(request, foto_id):
    foto = Fotos_BD.objects.get(pk=foto_id)
    like, created = Like_BD.objects.get_or_create(autor=request.user, foto=foto)
    if created:
        like.save()
    return redirect('index')

# -----> Comment ADD
def add_comentario(request, foto_id):
    foto = get_object_or_404(Fotos_BD, pk=foto_id)
    comentario_text = request.POST.get('comentario')
    if comentario_text:
        comentario = Comentarios_BD(comentario=comentario_text, autor=request.user)
        comentario.save()
        foto.comentarios_bd_set.add(comentario)
        foto.save()
    return redirect('index')

# -----> LOGIN LOGOUT AUTH
def login_view(request):
    user_form = LoginForms()

    if request.method == 'POST':
        user_form = LoginForms(request.POST)

    if user_form.is_valid():
        email = user_form['email'].value()
        senha = user_form['senha'].value()
        user_temp = User.objects.get(email=email)

        usuario = auth.authenticate(
            request,
            username = user_temp,
            password = senha
        )

        if usuario is not None:
            auth.login(request, usuario)
            messages.success(request, 'Foi logado com sucesso!')
            if usuario.is_staff:
                return redirect('dashboard')
            else:
                return redirect('index')
        else:
            messages.error(request, 'Erro ao efetuar login')
            return redirect('index')

    return render(request, 'index.html', {'user_form': user_form})

@login_required
def logout_view(request):
    auth.logout(request)
    messages.success(request, 'Logout efetuado com sucesso!')
    return redirect('index')

# -----> CRUD FOTOS
@login_required
def listarFotos(request):
    search_query = request.GET.get('search')
    if search_query:
        fotos = Fotos_BD.objects.filter(Q(titulo__icontains=search_query) | Q(autor__username__icontains=search_query))
    else:
        fotos = Fotos_BD.objects.all()
    return render(request,"dashboardConsulta_fotos.html",{"fotos":fotos})

@login_required
def edit_fotos(request, id):
    fotos = Fotos_BD.objects.get(pk=id)
    return render(request, "dashboardEditar_fotos.html",{'fotos':fotos})

@login_required
def update_fotos(request, id):
    fotos = Fotos_BD.objects.get(pk=id)
    fotos.titulo = request.POST['titulo']
    fotos.descricao = request.POST['descricao']
    fotos.foto = request.FILES['foto']
    fotos.save()
    return redirect('listarFotos')

@login_required
def delete_fotos(request, id):
    fotos = Fotos_BD.objects.get(pk=id)
    fotos.delete()
    return redirect('listarFotos')

# ------> CRUD USERS

@login_required
def edit_user(request, id):
    user = User.objects.get(pk=id)
    return render(request, "dashboardEditar_user.html",{'user':user})

@login_required
def update_user(request, id):
    user = User.objects.get(pk=id)
    user.username = request.POST['username']
    user.email = request.POST['email']
    user.save()
    return redirect('consulta_users')

@login_required
def delete_user(request, id):
    user = User.objects.get(pk=id)
    user.delete()
    return redirect('consulta_users')