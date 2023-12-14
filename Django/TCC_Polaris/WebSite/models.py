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

STATUS = (
    ('Pendente','Pendente'),
    ('Aprovado','Aprovado'),
    ('Cancelado','Cancelado'),
    ('Entregue','Entregue'),
)

PAIS = (
    ('BR','Brasil'),
)

ESTADOS = (
    ('AC', 'Acre'),
    ('AL', 'Alagoas'),
    ('AP', 'Amapá'),
    ('AM', 'Amazonas'),
    ('BA', 'Bahia'),
    ('CE', 'Ceará'),
    ('DF', 'Distrito Federal'),
    ('ES', 'Espírito Santo'),
    ('GO', 'Goiás'),
    ('MA', 'Maranhão'),
    ('MT', 'Mato Grosso'),
    ('MS', 'Mato Grosso do Sul'),
    ('MG', 'Minas Gerais'),
    ('PA', 'Pará'),
    ('PB', 'Paraíba'),
    ('PR', 'Paraná'),
    ('PE', 'Pernambuco'),
    ('PI', 'Piauí'),
    ('RJ', 'Rio de Janeiro'),
    ('RN', 'Rio Grande do Norte'),
    ('RS', 'Rio Grande do Sul'),
    ('RO', 'Rondônia'),
    ('RR', 'Roraima'),
    ('SC', 'Santa Catarina'),
    ('SP', 'São Paulo'),
    ('SE', 'Sergipe'),
    ('TO', 'Tocantins'),
)
class Pedido_BD(models.Model):
    produto = models.ForeignKey(Produtos_BD, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    endereco_entrega = models.TextField(max_length=255)
    pais = models.CharField(max_length =20, choices = PAIS ,default="BR")
    estado = models.CharField(max_length = 20, choices = ESTADOS, default='MG')
    cep = models.CharField(max_length=9, default=36680000)
    quantidade = models.PositiveIntegerField(default=1)
    total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    status = models.CharField(max_length = 20, choices = STATUS, default = 'Pendente')
    data_pedido = models.DateField(default=timezone.now)

    def save(self, *args, **kwargs):
        # Calcule o total com base na quantidade e preço do produto
        self.total = self.produto.preco * self.quantidade
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Pedido de {self.produto.titulo} por {self.nome}"