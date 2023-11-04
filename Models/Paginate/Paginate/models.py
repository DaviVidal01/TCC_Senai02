from django.db import models
from uuid import uuid4

# Create your models here.

def upload_image_foto(instance, filename):
    return f"{instance.id_foto}-{filename}"

class Fotos(models.Model):
    id_foto = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    titulo = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to=upload_image_foto, blank=True, null=True)
    autor = models.CharField(max_length=100)
    # Adicione outros campos conforme necessário

    def __str__(self):
        return self.titulo