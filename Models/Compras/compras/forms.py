from django import forms
from .models import Produto, Pedido

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'descricao', 'preco']

class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['nome_cliente', 'email_cliente', 'endereco_entrega', 'quantidade']
