from django.shortcuts import render
from .models import Like_BD, Fotos_BD, Comentarios_BD

def index(request):
    likes_view = Like_BD.objects.all()
    fotos_view = Fotos_BD.objects.all()
    comentarios_view = Comentarios_BD.objects.all()
    return render(request, 'index.html', {'likes': likes_view,'fotos': fotos_view,'comentarios': comentarios_view})

def detalhes_fotos(request):
    likes_view = Like_BD.objects.all()
    fotos_view = Fotos_BD.objects.all()
    comentarios_view = Comentarios_BD.objects.all()
    return render(request, 'detalhes_fotos.html', {'likes': likes_view,'fotos': fotos_view,'comentarios': comentarios_view})

def dashboard(request):
    return render(request, 'dashboard.html')

# Espaço reservado para o C.R.U.D do Dashboard!!!

# Consultar Fotos pelo C.R.U.D


# Adicionar Fotos pelo C.R.U.D
#def adicionarFoto(request):
#    foto = Fotos_BD.objects.all()
#    addfoto = AddFoto()
#    return render(request,"add_foto.html", {'foto': foto, 'addfoto': addfoto}