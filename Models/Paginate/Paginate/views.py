from django.shortcuts import render
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from .models import Fotos
from .models import *

# Create your views here.

def index(request):
    lista_de_fotos = Fotos.objects.all()  # Consulta para obter todas as fotos

    paginator = Paginator(lista_de_fotos, 10) # 5 fotos por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'paginate-test.html', {'page_obj': page_obj})

def fotosDoCatalogo(request):
    imagens = Fotos.objects.all()
    return render(request, 'paginate-test', {'imagens': imagens})