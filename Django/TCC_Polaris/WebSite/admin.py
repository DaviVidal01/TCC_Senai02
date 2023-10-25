from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Like_BD)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('like', 'autor')

@admin.register(Comentarios_BD)
class ComentariosAdmin(admin.ModelAdmin):
    list_display = ('comentario', 'autor', 'data_comentario')
    list_filter = ('autor', 'data_comentario')

@admin.register(Fotos_BD)
class FotosAdmin(admin.ModelAdmin):
    search_fields = ('titulo', 'autor')
    list_display = ('titulo', 'autor', 'data_foto')
    list_filter = ('autor', 'data_foto')
    fieldsets = [
        ('Informações Básicas', {'fields': ['titulo', 'autor', 'data_foto']}),
        ('Detalhes Adicionais', {'fields': ['images']}),
    ]
