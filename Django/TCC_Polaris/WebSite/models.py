from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from django.contrib.auth.models import User
# Create your models here.

class Tamanho_BD(models.Model):
    tamanho = models.CharField(max_length=7)

class Marca_BD(models.Model):
    marca = models.CharField(max_length=15)

class Tipo_BD(models.Model):
    tipo = models.CharField(max_length=15)

class Tecido_BD(models.Model):
    tecido = models.CharField(max_length=15)

class Produtos_BD(models.Model):
    titulo = models.CharField(max_length=25)
    foto = models.ImageField(upload_to= 'images/')
    descricao = models.TextField(max_length=255)
    preco = models.TextField(max_length=255)
    tamanho = models.ForeignKey(Tamanho_BD, on_delete=models.CASCADE)
    tipo = models.ForeignKey(Tipo_BD, on_delete=models.CASCADE)
    marca = models.ForeignKey(Marca_BD, on_delete=models.CASCADE)
    tecido = models.ForeignKey(Tecido_BD, on_delete=models.CASCADE)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    data_foto = models.DateField(default=timezone.now)
    
#-----Imagem da Barra de Pesquisa
class Barra_Pesquisa(models.Model):
    imagem = models.ImageField(upload_to= 'images/')