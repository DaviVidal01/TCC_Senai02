from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Comentarios_BD(models.Model):
    comentario = models.TextField(max_length=255)
    data_comentario = models.DateField()
    autor = models.ForeignKey(User.username)

class Like_BD(models.Model):
    like = models.IntegerField()
    autor = models.ForeignKey(User.username)

class Fotos_BD(models.Model):
    titulo = models.CharField(max_length=25)
    descricao = models.TextField(max_length=255)
    autor = models.ForeignKey(User.username)
    
