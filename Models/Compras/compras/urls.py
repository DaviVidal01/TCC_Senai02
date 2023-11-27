from django.urls import path
from . import views

urlpatterns = [
    path('', views.compras, name='compras'),
    path('listar/', views.listar_produtos, name='listar_produtos'),
    path('adicionar/', views.adicionar_produto, name='adicionar_produto'),
    path('efetuar_compra/<int:produto_id>/', views.efetuar_compra, name='efetuar_compra'),
    path('delete_produto/<int:produto_id>/', views.delete_produto, name="delete_produto"),
]
