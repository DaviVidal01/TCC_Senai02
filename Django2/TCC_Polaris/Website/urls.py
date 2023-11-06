from django.urls import path
from . import views
from Website.views import *

urlpatterns = [
    # -----> USER PAGE
    path('', views.index, name='index'),
    path('detalhes_fotos/', views.detalhes_fotos, name='detalhes_fotos'),
    # -----> ADMIN PAGE
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add_fotos/', views.add_fotos, name='add_fotos'),
    path('consulta_fotos/', views.consulta_fotos, name='consulta_fotos'),
    # -----> LOGIN AUTH
    path('inativar/<int:id>', views.inative, name="inative_user"),
    path('ativar/<int:id>', views.active, name="active_user"),
    path('login_user/', views.login_user, name="login_user"),
    path('logout/', views.logout_user, name="logout"),
    path('register_user/', views.register_user, name='register_user')
]