from django.db import models

class Fotos(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    # Adicione outros campos conforme necessário

    def __str__(self):
        return self.titulo

# Create your models here.
