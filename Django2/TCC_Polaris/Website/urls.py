from django.urls import path
from . import views
from Website.views import *

urlpatterns = [
    path('', views.index, name='index'),
    path('detalhes_fotos/', views.detalhes_fotos, name='detalhes_fotos'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('inativar/<int:id>', inative, name="inative_user"),
    path('ativar/<int:id>', active, name="active_user"),
]