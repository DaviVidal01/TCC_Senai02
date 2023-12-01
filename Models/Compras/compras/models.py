from django.contrib.auth.models import User
from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nome

class Pedido(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    email_cliente = models.EmailField()
    endereco_entrega = models.TextField()
    quantidade = models.PositiveIntegerField(default=1)
    total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    data_pedido = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Calcule o total com base na quantidade e preço do produto
        self.total = self.produto.preco * self.quantidade
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Pedido de {self.produto.nome} por {self.nome_cliente}"
