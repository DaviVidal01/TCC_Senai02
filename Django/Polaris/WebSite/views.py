from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse('<h1>Olá mundo.</h1>')

def pagina(request):
    return render(request,'index.html')