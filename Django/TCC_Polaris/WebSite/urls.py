from django.urls import path
from . import views

urlpatterns = [
    # -----> USER PAGE
    path('', views.index, name='index'),
    path('detalhes_fotos/', views.detalhes_fotos, name='detalhes_fotos'),
    # -----> ADMIN PAGE
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add_fotos/', views.add_fotos, name='add_fotos'),
    path('add_comentario/<int:foto_id>/', views.add_comentario, name='add_comentario'),
    path('consulta_fotos/', views.consulta_fotos, name='consulta_fotos'),
    path('consulta_users/', views.consulta_users, name='consulta_users'),
    # -----> LOGIN AUTH
    path('login', views.login_view, name="login"),
    path('logout', views.logout_view, name="logout"),
    path('add_user/', views.add_user, name='add_user'),
    # -----> CRUD FOTOS
    path('listarFotos', views.listarFotos, name="listarFotos"),
    path('editar/<int:id>', views.edit, name="edit"),
    path('atualizar/<int:id>', views.update, name="update"),
    path('deletar/<int:id>', views.delete, name="delete"),
]