from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from django.contrib.auth.models import User
# Create your models here.

class Comentarios_BD(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    comentario = models.TextField()
    data_comentario = models.DateField(default=timezone.now)

    def __str__(self):
        return f"Comentário por {self.autor} em {self.foto.titulo}"

class Like_BD(models.Model):
    like = models.IntegerField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)

class Fotos_BD(models.Model):
    titulo = models.CharField(max_length=25)
    descricao = models.TextField(max_length=255)
    data_foto = models.DateField(default=timezone.now)
    foto = models.ImageField(upload_to= 'images/')
    autor = models.ForeignKey(User, on_delete=models.CASCADE)

#-----Imagem da Barra de Pesquisa
class Barra_Pesquisa(models.Model):
    imagem = models.ImageField(upload_to= 'images/')