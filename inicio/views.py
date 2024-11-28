from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from datetime import date
from app_funcionalidad.models import Publicacion,Categoria,Usuario,Likes,Comentario,Convocatoria,Producto
from registrar.decorators import login_required_custom

# def ini(request):
#     publicaciones = Publicacion.objects.all().order_by('-id_publicacion')
#     usuario_id = request.session.get('id_usuario')
#     usuario = Usuario.objects.get(id_usuario=usuario_id) if usuario_id else None

#     # Agregar comentarios a las publicaciones
#     for publicacion in publicaciones:
#         publicacion.comentarios = Comentario.objects.filter(
#             tipo_entidad='publicacion',
#             id_entidad=publicacion.id_publicacion
#         ).order_by('-fecha_comentario')  # Ordenar por fecha si es necesario

#     context = {
#         'publicaciones': publicaciones,
#         'tipo_entidad': 'publicacion',
#     }
#     return render(request, 'inicio/inicio.html', context)


def ini(request):
    usuario_id = request.session.get("id_usuario")
    usuario = Usuario.objects.get(id_usuario=usuario_id) if usuario_id else None

    # Publicaciones
    publicaciones = Publicacion.objects.all().order_by("-id_publicacion")
    for publicacion in publicaciones:
        publicacion.comentarios = Comentario.objects.filter(
            tipo_entidad="publicacion", id_entidad=publicacion.id_publicacion
        ).order_by("-fecha_comentario")

    # Convocatorias
    convocatorias = Convocatoria.objects.all().order_by("-id_convocatoria")
    id_categoria = request.GET.get("categoria", "")
    categorias = Categoria.objects.all()


    for convocatoria in convocatorias:
        convocatoria.comentarios = Comentario.objects.filter(
            id_entidad=convocatoria.id_convocatoria, tipo_entidad="convocatoria"
        )

    context = {
        "usuario": usuario,
        "publicaciones": publicaciones,
        "convocatorias": convocatorias,
    }

    return render(request, "inicio/inicio.html", context)




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


# comentarios

# Vista para crear un comentario
# def crear_comentario(request, tipo_entidad, id_entidad):
#     usuario_id = request.session.get('id_usuario')
#     usuario = Usuario.objects.get(id_usuario=usuario_id) if usuario_id else None
    
#     if not usuario:
#         return HttpResponse("Debes iniciar sesión para comentar.", status=403)

#     # Obtener la entidad dependiendo del tipo
#     if tipo_entidad == 'convocatoria':
#         entidad = get_object_or_404(Convocatoria, pk=id_entidad)
#     elif tipo_entidad == 'producto':
#         entidad = get_object_or_404(Producto, pk=id_entidad)
#     elif tipo_entidad == 'publicacion':
#         entidad = get_object_or_404(Publicacion, pk=id_entidad)
#     else:
#         return HttpResponse("Tipo de entidad no válido.", status=400)

#     # Procesar el formulario de comentario
#     if request.method == 'POST':
#         texto = request.POST.get('texto')
        
#         # Crear el comentario
#         Comentario.objects.create(
#             id_usuario=usuario,
#             tipo_entidad=tipo_entidad,
#             id_entidad=id_entidad,
#             texto=texto
#         )
        
#         # Redireccionar a la página anterior
#         return redirect(request.META.get('HTTP_REFERER', 'publicaciones'))

#     return HttpResponse("Método no permitido", status=405)




def crear_comentario(request, tipo_entidad, id_entidad):
    # Verificar que el usuario está autenticado
    usuario_id = request.session.get('id_usuario')
    usuario = Usuario.objects.get(id_usuario=usuario_id) if usuario_id else None
    if not usuario:
        return HttpResponse("Debes iniciar sesión para comentar.", status=403)

    # Validar tipo de entidad y obtener la entidad correspondiente
    if tipo_entidad == 'convocatoria':
        entidad = get_object_or_404(Convocatoria, pk=id_entidad)
        redirect_url = 'convocatorias'  # Nombre de la vista o ruta para redirección
    elif tipo_entidad == 'publicacion':
        entidad = get_object_or_404(Publicacion, pk=id_entidad)
        redirect_url = 'inicio'  # Nombre de la vista o ruta para redirección
    else:
        return HttpResponse("Tipo de entidad no válido.", status=400)

    # Procesar la creación del comentario
    if request.method == 'POST':
        texto = request.POST.get('texto')
        if not texto:
            return HttpResponse("El comentario no puede estar vacío.", status=400)

        Comentario.objects.create(
            id_usuario=usuario,
            tipo_entidad=tipo_entidad,
            id_entidad=id_entidad,
            texto=texto
        )
        # Redirigir a la página anterior o a la vista correspondiente
        return redirect(request.META.get('HTTP_REFERER', redirect_url))

    return HttpResponse("Método no permitido", status=405)