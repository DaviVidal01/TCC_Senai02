from .models import Produto, Compra
from .forms import ProdutoForm
from django.shortcuts import render, redirect, get_object_or_404

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

    # Crie uma nova compra
    nova_compra = Compra(produto=produto)
    nova_compra.save()
    # Lógica adicional pode ser adicionada aqui, como atualizar o estoque, processar pagamento, etc.

    # Redirecione para a lista de produtos após a compra
    return redirect('listar_produtos')