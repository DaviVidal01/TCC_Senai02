from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

GENERO = (
    ('Masculino','Masculino'),
    ('Feminino','Feminino'),
    ('Unisex','Unisex'),
)

class Tamanho_BD(models.Model):
    tamanho = models.CharField(max_length=7)
    def __str__(self):
        return self.tamanho

class Marca_BD(models.Model):
    marca = models.CharField(max_length=15)
    def __str__(self):
        return self.marca

class Tipo_BD(models.Model):
    tipo = models.CharField(max_length=15)
    def __str__(self):
        return self.tipo

class Tecido_BD(models.Model):
    tecido = models.CharField(max_length=15)
    def __str__(self):
        return self.tecido

class Produtos_BD(models.Model):
    titulo = models.CharField(max_length=25)
    foto = models.ImageField(upload_to= 'images/')
    descricao = models.TextField(max_length=255)
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    genero = models.CharField(max_length = 20, choices = GENERO, default = 'Unisex')
    tamanho = models.ForeignKey(Tamanho_BD, on_delete=models.CASCADE)
    tipo = models.ForeignKey(Tipo_BD, on_delete=models.CASCADE)
    marca = models.ForeignKey(Marca_BD, on_delete=models.CASCADE)
    tecido = models.ForeignKey(Tecido_BD, on_delete=models.CASCADE)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    data_foto = models.DateField(default=timezone.now)
    
#-----Imagem da Barra de Pesquisa
class Barra_Pesquisa(models.Model):
    imagem = models.ImageField(upload_to= 'images/')

# * ATENÇÃO ESTA PARTE DAS MODELS VAI FAZER O CHECKOUT, OU SEJA AS COMPRAS *
# * ATENÇÃO, O NOME DA CLASSE É 'PEDIDO' E EFETUA A FUNÇÃO DE CHECKOUT *
# * ATENÇÃO ESTA FASE ANDA ESTÁ EM FASE DE TESTES!! *
class Pedido(models.Model):
    produto = models.ForeignKey(Produtos_BD, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    email = models.EmailField()
    endereco_entrega = models.TextField()
    quantidade = models.PositiveIntegerField(default=1)
    total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    data_pedido = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Calcule o total com base na quantidade e preço do produto
        self.total = self.produto.preco * self.quantidade
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Pedido de {self.produto.titulo} por {self.nome}"