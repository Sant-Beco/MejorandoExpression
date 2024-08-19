from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def publicaciones_admin(request):
    return render(request, 'admin_publicaciones/publicaciones_admin.html')
