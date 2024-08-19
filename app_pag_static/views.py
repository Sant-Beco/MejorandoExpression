from django.shortcuts import render

# Create your views here.
def base_pag_static(request):
  return render(request, 'app_pag_static/base_pag_static.html')

def acerca_nosotros(request):
  return render(request, 'app_pag_static/acerca_nosotros.html')

def reglas_negocio(request):
  return render(request, 'app_pag_static/reglas_negocio.html')

def terminos_condiciones(request):
  return render(request, 'app_pag_static/terminos_condiciones.html')

def vista_principal(request):
  return render(request, 'app_pag_static/vista_principal.html')
