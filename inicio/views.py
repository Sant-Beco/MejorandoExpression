from django.shortcuts import render,redirect
from app_funcionalidad.models import Usuario, Publicacion, Convocatoria,Producto
from registrar.decorators import login_required_custom

@login_required_custom
def ini(request):
    lista_p = Publicacion.objects.all()
    lista_c = Convocatoria.objects.all()
    lista = Producto.objects.all()
    usuario = Usuario.objects.all()
    return render(request, 'inicio/inicio.html',{'usuario':usuario,
                                                    'lista_p':lista_p ,
                                                    'lista_c':lista_c,
                                                    'lista':lista})