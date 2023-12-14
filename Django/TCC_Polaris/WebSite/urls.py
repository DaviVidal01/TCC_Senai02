from django.urls import path
from . import views

urlpatterns = [
    # -----> USER PAGE
    path('',views.index,name='index'),
    path('sobre/',views.sobre,name='sobre'),
    path('dicas/',views.dicas,name='dicas'),
    path('faq/',views.faq,name='faq'),
    path('termos/',views.termos,name='termos'),
    path('politica/',views.politica,name='politica'),
    path('catalogo/', views.catalogo, name='catalogo'),
    # -----> CHECKOUT
    path('efetuar_compra/<int:produto_id>/', views.efetuar_compra, name='efetuar_compra'),
    # -----> ADMIN PAGE
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add_fotos/', views.add_fotos, name='add_fotos'),
    path('add_user/', views.add_user, name='add_user'),
    path('consulta_fotos/', views.consulta_fotos, name='consulta_fotos'),
    path('consulta_users/', views.consulta_users, name='consulta_users'),
    path('consulta_pedidos/', views.consulta_pedidos, name='consulta_pedidos'),
    # -----> LOGIN AUTH
    path('login', views.login_view, name="login"),
    path('register', views.register_view, name="register"),
    path('logout', views.logout_view, name="logout"),
    # -----> CRUD FOTOS
    path('listarFotos', views.listarFotos, name="listarFotos"),
    path('editar_fotos/<int:id>', views.edit_fotos, name="edit_fotos"),
    path('atualizar_fotos/<int:id>', views.update_fotos, name="update_fotos"),
    path('deletar_fotos/<int:id>', views.delete_fotos, name="delete_fotos"),
    # -----> CRUD USER
    path('listarUsers', views.listarUsers, name="listarUsers"),
    path('editar_user/<int:id>', views.edit_user, name="edit_user"),
    path('atualizar_user/<int:id>', views.update_user, name="update_user"),
    path('deletar_user/<int:id>', views.delete_user, name="delete_user"),
    # -----> CRUD PEDIDOS
    path('listarPedidos', views.listarPedidos, name="listarPedidos"),
    path('aprovar_pedido/<int:id>', views.aprovar_pedido, name="aprovar_pedido"),
    path('cancelar_pedido/<int:id>', views.cancelar_pedido, name="cancelar_pedido"),
    path('deletar_pedido/<int:id>', views.delete_pedido, name="delete_pedido"),
    path('entregar_pedido/<int:id>', views.entregar_pedido, name="entregar_pedido"),
]