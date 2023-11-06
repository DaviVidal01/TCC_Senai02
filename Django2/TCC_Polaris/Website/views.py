from django.shortcuts import render,redirect
from Website.forms import LoginForms, RegisterForms
from .models import Like_BD, Fotos_BD, Comentarios_BD
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def index(request):
    likes_view = Like_BD.objects.all()
    fotos_view = Fotos_BD.objects.all()
    comentarios_view = Comentarios_BD.objects.all()
    return render(request, 'index.html', {'likes': likes_view,'fotos': fotos_view,'comentarios': comentarios_view})

def detalhes_fotos(request):
    likes_view = Like_BD.objects.all()
    fotos_view = Fotos_BD.objects.all()
    comentarios_view = Comentarios_BD.objects.all()
    return render(request, 'detalhes_fotos.html', {'likes': likes_view,'fotos': fotos_view,'comentarios': comentarios_view})


@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

# Espaço reservado para o C.R.U.D do Dashboard!!!

# Consultar Fotos pelo C.R.U.D


# Adicionar Fotos pelo C.R.U.D
#def adicionarFoto(request):
#    foto = Fotos_BD.objects.all()
#    addfoto = AddFoto()
#    return render(request,"add_foto.html", {'foto': foto, 'addfoto': addfoto}

def login(request):
    form = LoginForms()

    if request.method == 'POST':
        form = LoginForms(request.POST)

        if form.is_valid():
            email = form['email'].value()
            password = form['senha'].value()
        user_temp = User.objects.get(email= email)

        user = auth.authenticate(
            request,
            username=user_temp,
            password=password
        )

        if user is not None:
            auth.login(request, user)
            messages.success(request, f'Foi logado com sucesso!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Erro ao efetuar login')
            return redirect('login')

    return render(request, 'usuarios/login.html', {'form': form})

@login_required
def register(request):
    if request.method == 'POST':
        form = RegisterForms(request.POST)

        if form.is_valid():
            name=form['name'].value()
            email=form['email'].value()
            password=form['password'].value()

            if User.objects.filter(username=name).exists():
                messages.error(request, 'Usuário já existente')
                return redirect('users')

            usuario = User.objects.create_user(
                username=name,
                email=email,
                password=password
            )
            usuario.save()
            messages.success(request, 'Usuario cadastrado com sucesso!')
            return redirect('users')

@login_required
def logout(request):
    auth.logout(request)
    messages.success(request, 'Logout efetuado com sucesso!')
    return redirect('login')

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