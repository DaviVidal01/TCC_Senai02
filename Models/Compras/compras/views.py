from .models import Produto, Pedido
from .forms import ProdutoForm, CheckoutForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
def compras(request):
    return render(request, 'compras.html')

def listar_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'listar_produtos.html', {'produtos': produtos})

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


def efetuar_compra(request, produto_id):
    produto = Produto.objects.get(id=produto_id)
    
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

    return render(request, 'efetuar_compra.html', {'form': form, 'produto': produto})
