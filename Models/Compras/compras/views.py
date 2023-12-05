from django.contrib import messages
from django.conf import settings
from .models import Produto, Pedido
from .forms import ProdutoForm, CheckoutForm
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage

# Create your views here.
def compras(request):
    # Obtém o parâmetro de ID da solicitação GET
    produto_id = request.GET.get('id')

    # Se um ID foi fornecido, filtra o produto pelo ID
    if produto_id:
        produto = get_object_or_404(Produto, id=produto_id)
        # Retorna apenas o produto específico
        return render(request, 'compras.html', {'produto': produto})
    else:
        # Se nenhum ID foi fornecido, lista todos os produtos
        produtos = Produto.objects.all()
        return render(request, 'compras.html', {'produtos': produtos})

def listar_produtos(request):
    # Obtém o parâmetro de ID da solicitação GET
    produto_id = request.GET.get('id')

    # Se um ID foi fornecido, filtra o produto pelo ID
    if produto_id:
        produto = get_object_or_404(Produto, id=produto_id)
        # Retorna apenas o produto específico
        return render(request, 'listar_produtos.html', {'produto': produto, 'quantidade_produtos': Produto.objects.count()})
    else:
 # Se nenhum ID foi fornecido, lista todos os produtos
        produtos = Produto.objects.all()
        return render(request, 'listar_produtos.html', {'produtos': produtos, 'quantidade_produtos': Produto.objects.count()})

def compras(request):
    produtos = Produto.objects.all()

    # Número de itens por página
    items_por_pagina = 5  # Altere conforme necessário

    # Obtém o número da página a partir dos parâmetros da solicitação
    page = request.GET.get('page', 1)

    # Cria um objeto Paginator
    paginator = Paginator(produtos, items_por_pagina)

    try:
        produtos_paginados = paginator.page(page)
    except EmptyPage:
        # Se a página solicitada estiver fora do intervalo, exibe a última página disponível
        produtos_paginados = paginator.page(paginator.num_pages)

    return render(request, 'compras.html', {'produtos': produtos_paginados })


def adicionar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_produtos')
    else:
        form = ProdutoForm()
    return render(request, 'adicionar_produto.html', {'form': form})

#Deletar produtos
def delete_produto(request, produto_id):
    produto = Produto.objects.get(id=produto_id)
    produto.delete()
    return redirect('listar_produtos')

#   ATENÇÃO ESTA PARTE DAS MODELS EFETUA AS COMPRAS E AINDA ESTÁ SOB FASE DE TESTE   #
def efetuar_compra(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            # Crie um novo pedido
            novo_pedido = form.save(commit=False)
            novo_pedido.produto = produto
            novo_pedido.save()

            # Lógica adicional pode ser adicionada aqui, como atualizar o estoque, processar pagamento, etc.

            # Redirecione para a lista de produtos após a compra
            return redirect('listar_produtos')
    else:
        form = CheckoutForm()
        
    context = {'form': form, 'produto': produto}
    return render(request, 'efetuar_compra.html', {'form': form, 'produto': produto})

#   ATENÇÃO ESTA PARTE TEM A FUNÇÃO DE FAZER A QUANTIDADE DOS PRODUTOS E CRIAR O VALOR TOTAL E AINDA ESTÁ SOB FASE DE TESTE   #

def detalhes_produto(request, produto_id):
    produto = Produto.objects.get(pk=produto_id)
    pedido = Pedido(produto=produto, quantidade=1)  # Defina outros campos conforme necessário

    context = {
        'produto': produto,
        'pedido': pedido,
    }
    return render(request, 'efetuar_compra.html', context)