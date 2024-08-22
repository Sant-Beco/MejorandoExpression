from django.shortcuts import render, get_object_or_404,redirect
from app_perfil.forms import  UsuarioForm
from app_funcionalidad.models import Usuario, Publicacion, Convocatoria,Producto
from django.contrib.auth import logout


def perfil(request):
    usuario_id = request.session.get('id_usuario')
    usuario = None
    if usuario_id:
        try:
            usuario = Usuario.objects.get(id_usuario=usuario_id)
        except Usuario.DoesNotExist:
            usuario = None
    # Filtrar las publicaciones para mostrar solo las del usuario actual
    lista_p = Publicacion.objects.filter(id_usuario=usuario_id).order_by('-id_publicacion') if usuario else []
    lista_c = Convocatoria.objects.filter(id_usuario=usuario_id).order_by('-id_convocatoria') if usuario else []
    lista = Producto.objects.filter(id_usuario=usuario_id).order_by('-id_producto') if usuario else []
    return render(request, 'app_perfil/perfil.html', {
        'usuario': usuario,
        'lista_p': lista_p,
        'lista_c': lista_c,
        'lista': lista
    })
#EDITAR EL PERFIL DE DATOS PERSONALES
def update(request, id_usuario):
    usuario_id = request.session.get('id_usuario')
    usuario = None
    if usuario_id:
        try:
            usuario = Usuario.objects.get(id_usuario=usuario_id)
        except Usuario.DoesNotExist:
            usuario = None
    formulario = UsuarioForm(instance=usuario)
    if request.method =='POST':
        formulario = UsuarioForm(request.POST, request.FILES, instance=usuario)
        if formulario.is_valid():
            formulario.save()
            return redirect('perfil')
    return render(request, 'app_perfil/update.html', {'formulario': formulario,'usuario': usuario})

def delete_publicacion(request, id_publicacion):
    publicacion = get_object_or_404(Publicacion, id_publicacion=id_publicacion)
    publicacion.delete()
    return redirect('perfil')


def delete_convocatoria(request, id_convocatoria):
    convo = get_object_or_404(Convocatoria, id_convocatoria=id_convocatoria)
    convo.delete()
    return redirect('perfil')

def delete_producto(request, id_producto):
    produ = get_object_or_404(Producto, id_producto=id_producto)
    produ.delete()
    return redirect('perfil')


def logout_usu(request):
    logout(request)
    response = redirect('login')
    
    for cookie in request.COOKIES:    # Limpiar todas las cookies del navegador
        response.delete_cookie(cookie)
    
    return response