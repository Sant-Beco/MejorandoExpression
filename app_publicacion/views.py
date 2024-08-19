from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from datetime import date

from app_funcionalidad.models import Publicacion,Categoria,Usuario,Likes


# Create your views here.


def publicaciones(request):
    usuario_id = request.session.get('id_usuario')  # Asume que tienes el ID del usuario en la sesión
    usuario = Usuario.objects.get(id_usuario=usuario_id) if usuario_id else None
    id_categoria = request.GET.get('categoria', '')
    categorias = Categoria.objects.all()

    if id_categoria:
        publicaciones = Publicacion.objects.filter(id_categoria=id_categoria).order_by('-id_publicacion')
    else:
        publicaciones = Publicacion.objects.all().order_by('-id_publicacion')

    return render(request, 'app_publicacion/publicaciones.html', {
        'publicaciones': publicaciones,
        'categorias': categorias,
        'selected_categoria': int(id_categoria) if id_categoria else '',
        'usuario': usuario
    })



def formulario_publicacion(request):
    if request.method == 'POST':
        titulo = request.POST['titulo']
        descripcion = request.POST['descripcion']
        foto = request.FILES.get('foto')
        categoria_id = int(request.POST['categorias'])

        usuario_id = request.session.get('id_usuario')  # O el método que estás usando para obtener el ID

        try:
            # Obtener la instancia del usuario correspondiente
            usuario = Usuario.objects.get(id_usuario=usuario_id)
        except Usuario.DoesNotExist:
            return HttpResponse("Usuario no encontrado", status=404)

        publicacion = Publicacion(
            id_usuario=usuario,  # Aquí asignamos la instancia del usuario
            id_categoria_id=categoria_id,
            titulo=titulo,
            descripcion=descripcion,
            foto=foto,
            fecha_publicacion=date.today(),
        )
        publicacion.save()
        return redirect('publicaciones')

    categorias = Categoria.objects.all()
    return render(request, 'app_publicacion/formulario_publicacion.html', {'categorias': categorias})


@require_POST
def like(request, tipo_entidad, id_entidad):
    # Obtener el usuario actual
    usuario_id = request.session.get('id_usuario')
    usuario = Usuario.objects.get(id_usuario=usuario_id)
    if tipo_entidad == 'publicacion':
        entidad = get_object_or_404(Publicacion, pk=id_entidad)
    if Likes.objects.filter(id_usuario=usuario, tipo_entidad=tipo_entidad, id_entidad=id_entidad).exists():
        return HttpResponse("Ya has dado like a esta entidad.", status=400)
    Likes.objects.create(id_usuario=usuario, tipo_entidad=tipo_entidad, id_entidad=id_entidad)
    return redirect(request.META.get('HTTP_REFERER', 'publicaciones'))




