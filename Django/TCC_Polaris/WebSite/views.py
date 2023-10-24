from django.shortcuts import render
from .models import Like_BD, Fotos_BD, Comentarios_BD

def index(request):
    likes_view = Like_BD.objects.all()
    fotos_view = Fotos_BD.objects.all()
    comentarios_view = Comentarios_BD.objects.all()
    return render(request, 'index.html', {'likes': likes_view,'fotos': fotos_view,'comentarios': comentarios_view})

