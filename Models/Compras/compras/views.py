from django.shortcuts import render

# Create your views here.

def compras(request):
    return render(request, 'compras.html')
