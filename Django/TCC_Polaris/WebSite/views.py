from django.contrib import messages
from django.contrib import auth
from django.http import HttpResponseForbidden
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render, get_object_or_404, redirect
from Website.forms import ProdutosForms, CheckoutForm, LoginForms, RegisterForms, UserForms
from .models import Barra_Pesquisa, Pedido, Produtos_BD, Tipo_BD, Marca_BD, Tecido_BD, Tamanho_BD, GENERO
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from django.contrib.auth.decorators import user_passes_test
from django.core.paginator import Paginator, EmptyPage
from django.urls import reverse

# ------> VERIFICADORES
def is_admin(user):
    return user.is_staff

def admin_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_staff:
            return render(
                request,
                'error_page.html',
                {'error_message': "Você não tem permissão para acessar esta página."}
            )
        return view_func(request, *args, **kwargs)

    return _wrapped_view

# -----> USER PAGE
def index(request):
    fotos_view = Produtos_BD.objects.all()
    register_form = RegisterForms()
    login_form = LoginForms()
    imagem_view = Barra_Pesquisa.objects.all()
    user = User.objects.all()
    return render(request, 'index.html', {'register_form':register_form,'user_form': login_form , 'fotos': fotos_view,'imagens': imagem_view})

def faq(request):
    fotos_view = Produtos_BD.objects.all()
    register_form = RegisterForms()
    login_form = LoginForms()
    imagem_view = Barra_Pesquisa.objects.all()
    user = User.objects.all()
    return render(request, 'faq.html', {'register_form':register_form,'user_form': login_form ,'fotos': fotos_view,'imagens': imagem_view})

def termos(request):
    fotos_view = Produtos_BD.objects.all()
    register_form = RegisterForms()
    login_form = LoginForms()
    imagem_view = Barra_Pesquisa.objects.all()
    user = User.objects.all()
    return render(request, 'termos.html', {'register_form':register_form,'user_form': login_form ,'fotos': fotos_view,'imagens': imagem_view})

def politica(request):
    fotos_view = Produtos_BD.objects.all()
    register_form = RegisterForms()
    login_form = LoginForms()
    imagem_view = Barra_Pesquisa.objects.all()
    user = User.objects.all()
    return render(request, 'politica.html', {'register_form':register_form,'user_form': login_form ,'fotos': fotos_view,'imagens': imagem_view})

def dicas(request):
    fotos_view = Produtos_BD.objects.all()
    register_form = RegisterForms()
    login_form = LoginForms()
    imagem_view = Barra_Pesquisa.objects.all()
    user = User.objects.all()
    return render(request, 'dicas.html', {'register_form':register_form,'user_form': login_form ,'fotos': fotos_view,'imagens': imagem_view})

def sobre(request):
    fotos_view = Produtos_BD.objects.all()
    register_form = RegisterForms()
    login_form = LoginForms()
    imagem_view = Barra_Pesquisa.objects.all()
    user = User.objects.all()
    return render(request, 'sobre.html', {'register_form':register_form,'user_form': login_form ,'fotos': fotos_view,'imagens': imagem_view})

from django.core.paginator import Paginator, EmptyPage

def catalogo(request):
    # Código do primeiro bloco
    query = request.GET.get('q')
    genero_filter = request.GET.get('genero')
    tipo_filter = request.GET.get('tipo')
    marca_filter = request.GET.get('marca')
    tecido_filter = request.GET.get('tecido')
    tamanho_filter = request.GET.get('tamanho')

    produtos_view = Produtos_BD.objects.all()

    if query:
        produtos_view = produtos_view.filter(titulo__icontains=query)

    if genero_filter:
        produtos_view = produtos_view.filter(genero=genero_filter)

    if tipo_filter:
        produtos_view = produtos_view.filter(tipo__tipo=tipo_filter)

    if marca_filter:
        produtos_view = produtos_view.filter(marca__marca=marca_filter)

    if tecido_filter:
        produtos_view = produtos_view.filter(tecido__tecido=tecido_filter)

    if tamanho_filter:
        produtos_view = produtos_view.filter(tamanho__tamanho=tamanho_filter)

    register_form = RegisterForms()
    login_form = LoginForms()
    imagem_view = Barra_Pesquisa.objects.all()
    user = User.objects.all()

    tipos = Tipo_BD.objects.all()
    marcas = Marca_BD.objects.all()
    tecidos = Tecido_BD.objects.all()
    tamanhos = Tamanho_BD.objects.all()
    generos = [choice[0] for choice in GENERO]

    items_por_pagina = 10  # Altere conforme necessário

    # Obtém o número da página a partir dos parâmetros da solicitação
    page = request.GET.get('page', 1)

    # Cria um objeto Paginator
    paginator = Paginator(produtos_view, items_por_pagina)

    try:
        produtos_paginados = paginator.page(page)
    except EmptyPage:
        # Se a página solicitada estiver fora do intervalo, exibe a última página disponível
        produtos_paginados = paginator.page(paginator.num_pages)

    return render(request, 'catalogo.html', {
        'register_form':register_form,
        'user_form': login_form ,
        'produtos': produtos_paginados,
        'imagens': imagem_view,
        'generos': generos,
        'tipos': tipos,
        'marcas': marcas,
        'tecidos': tecidos,
        'tamanhos': tamanhos,
        'users': user
    })

#   ATENÇÃO ESTA PARTE DAS MODELS EFETUA AS COMPRAS E AINDA ESTÁ SOB FASE DE TESTE   #
def efetuar_compra(request, produto_id):
    produto = get_object_or_404(Produtos_BD, id=produto_id)
    
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            # Crie um novo pedido
            novo_pedido = form.save(commit=False)
            novo_pedido.produto = produto
            novo_pedido.save()

            # Lógica adicional pode ser adicionada aqui, como atualizar o estoque, processar pagamento, etc.

            # Redirecione para a lista de produtos após a compra
            return redirect('catalogo')
    else:
        form = CheckoutForm()
        
    context = {'form': form, 'produto': produto}
    return render(request, 'efetuar_compra.html', {'form': form, 'produto': produto})

#   ATENÇÃO ESTA PARTE TEM A FUNÇÃO DE FAZER A QUANTIDADE DOS PRODUTOS E CRIAR O VALOR TOTAL E AINDA ESTÁ SOB FASE DE TESTE   #

def detalhes_produto(request, produto_id):
    produto = Produtos_BD.objects.get(pk=produto_id)
    pedido = Pedido(produto=produto, quantidade=1)  # Defina outros campos conforme necessário

    context = {
        'produto': produto,
        'pedido': pedido,
    }
    return render(request, 'efetuar_compra.html', context)

# ATENÇÃO ESTE TRECHO SE TRATA DO ESQUECI MINHA SENHA E AINDA ESTÁ SOB TESTE
def esqueci_senha(request):
    # Sua lógica para a recuperação de senha aqui
    return render(request, 'catalogo.html')

# -----> DASHBOARD ADMIN PAGE

@admin_required
def dashboard(request):
    user = User.objects.all()
    fotos_view = Produtos_BD.objects.all()
    return render(request, 'dashboard.html', {'user':user,'fotos': fotos_view})

@admin_required
def consulta_fotos(request):
    user = User.objects.all()
    fotos_view = Produtos_BD.objects.all()
    return render(request, 'dashboardConsulta_fotos.html', {'user':user, 'fotos': fotos_view})

@admin_required
def consulta_users(request):
    user = User.objects.all()
    fotos_view = Produtos_BD.objects.all()
    return render(request, 'dashboardConsulta_user.html', {'user':user, 'fotos': fotos_view})

@admin_required
def add_user(request):
    try:
        if request.method == 'POST':
            register_form = UserForms(request.POST)
            if register_form.is_valid():
                user = register_form.save(commit=False)
                user.save()
                messages.success(request, 'Usuário foi adicionado com sucesso!')
                return redirect('add_user')    
        else:
            register_form = UserForms()
    except Exception as e:
        messages.error(request, e)

    return render(request, 'dashboardAdd_user.html', {'register_form': register_form})

@admin_required
def add_fotos(request):
    if request.method == 'POST':
        foto_form = ProdutosForms(request.POST, request.FILES)
        if foto_form.is_valid():
            foto = foto_form.save(commit=False)
            foto.autor = request.user
            foto.save()
            messages.success(request, 'Produto foi adicionado com sucesso!')
            return redirect('consulta_fotos')
    else:
        foto_form = ProdutosForms()

    return render(request, 'dashboardAdd_fotos.html', {'foto_form': foto_form})

# -----> LOGIN LOGOUT AUTH
def register_view(request):
    if request.method == 'POST':
        register_form = RegisterForms(request.POST)
        if register_form.is_valid():
            email = register_form.cleaned_data.get('email')
            username = register_form.cleaned_data.get('username')
            password = register_form.cleaned_data.get('password')
            user = User.objects.create_user(username=username, email=email, password=password)

            if user is not None:
                user = authenticate(request, username=username, password=password)
                login(request, user)
                return redirect('index')
            else:
                messages.error(request, 'Erro ao efetuar login')
                return redirect('index')
    else:
        register_form = RegisterForms()

    return render(request, 'index.html', {'register_form': register_form})

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
    messages.warning(request, 'Logout efetuado com sucesso!')
    return redirect('index')

# -----> CRUD FOTOS
@login_required
def listarFotos(request):
    search_query = request.GET.get('search')
    if search_query:
        fotos = Produtos_BD.objects.filter(Q(titulo__icontains=search_query) | Q(autor__username__icontains=search_query))
    else:
        fotos = Produtos_BD.objects.all()
    return render(request,"dashboardConsulta_fotos.html",{"fotos":fotos})

@login_required
def edit_fotos(request, id):
    fotos = Produtos_BD.objects.get(pk=id)
    form = ProdutosForms(instance=fotos)
    return render(request, "dashboardEditar_fotos.html",{'fotos':fotos, 'form':form})

@login_required
def update_fotos(request, id):
    try:
        fotos = Produtos_BD.objects.get(pk=id)
        form = ProdutosForms(request.POST, request.FILES, instance=fotos)

        if form.is_valid():
            # Se um novo arquivo for fornecido, atualiza o campo 'foto'
            form.save()
            messages.warning(request, 'Produto editado com sucesso!')
            return redirect('listarFotos')

    except Exception as e:
        messages.error(request, e)

    return redirect('listarFotos')

@login_required
def delete_fotos(request, id):
    fotos = Produtos_BD.objects.get(pk=id)
    fotos.delete()
    messages.error(request, 'Produto deletado com sucesso!')
    return redirect('listarFotos')

# ------> CRUD USERS

@login_required
def listarUsers(request):
    search_query = request.GET.get('search')
    if search_query:
        user = User.objects.filter(Q(username__icontains=search_query) | Q(email__icontains=search_query))
    else:
        user = User.objects.all()
    return render(request,"dashboardConsulta_user.html",{"user":user})

@login_required
def edit_user(request, id):
    try:
        user = User.objects.get(pk=id)
    except Exception as e:
        messages.error(request, e)
    return render(request, "dashboardEditar_user.html",{'user':user})

@login_required
def update_user(request, id):
    try:
        user = User.objects.get(pk=id)
        user.username = request.POST['username']
        user.email = request.POST['email']
        user.save()
        messages.warning(request, 'Usuário editado com sucesso!')
    except Exception as e:
        messages.error(request, e)

    return redirect('consulta_users')

@login_required
def delete_user(request, id):
    user = User.objects.get(pk=id)
    user.delete()
    messages.error(request, 'Usuário deletado com sucesso!')
    return redirect('consulta_users')