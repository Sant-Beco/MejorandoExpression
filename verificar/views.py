from django.shortcuts import render

# Create your views here.

def verificar(request):
    return render(request, 'verificar/verificarcodigo.html')