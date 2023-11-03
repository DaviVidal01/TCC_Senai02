from django.shortcuts import render
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from .models import Fotos

# Create your views here.

def index(request):
    lista_de_fotos = Fotos.objects.all()  # Consulta para obter todos os livros

    paginator = Paginator(lista_de_fotos, 4) # 10 livros por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'paginate-test.html', {'page_obj': page_obj})