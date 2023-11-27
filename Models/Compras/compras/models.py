from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nome
    
class Compra(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    data_compra = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Compra de {self.produto.nome} em {self.data_compra}"