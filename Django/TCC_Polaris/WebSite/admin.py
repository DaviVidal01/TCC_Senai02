from django.contrib import admin
from .models import Produtos_BD, Tecido_BD, Tipo_BD, Marca_BD, Tamanho_BD, Barra_Pesquisa

@admin.register(Tecido_BD)
class TecidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'tecido')
@admin.register(Tipo_BD)
class TipoAdmin(admin.ModelAdmin):
    list_display = ('id','tipo')
@admin.register(Marca_BD)
class MarcaAdmin(admin.ModelAdmin):
    list_display = ('id','marca')
@admin.register(Tamanho_BD)
class TamanhoAdmin(admin.ModelAdmin):
    list_display = ('id','tamanho')
admin.site.register(Produtos_BD)
admin.site.register(Barra_Pesquisa)
# Register your models here.
