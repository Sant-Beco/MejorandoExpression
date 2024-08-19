from django.shortcuts import render


# Create your views here.

def base(request):
  return render(request, 'app_funcionalidad/base.html')

def base_admin(request):
  return render(request, 'app_funcionalidad/base_admin.html')