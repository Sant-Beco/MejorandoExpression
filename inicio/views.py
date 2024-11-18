from app_funcionalidad.models import Usuario, Publicacion, Convocatoria,Producto
from registrar.decorators import login_required_custom
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from datetime import date
from app_funcionalidad.models import Publicacion,Categoria,Usuario,Likes,Comentario,Convocatoria,Producto
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



@login_required_custom
def publicaciones(request):
    publicaciones = Publicacion.objects.all().order_by('-id_publicacion')
    usuario_id = request.session.get('id_usuario')
    usuario = Usuario.objects.get(id_usuario=usuario_id) if usuario_id else None
    id_categoria = request.GET.get('categoria', '')
    categorias = Categoria.objects.all()

    # Filtrar publicaciones por categoría si se proporciona una
    if id_categoria.isdigit():
        publicaciones = publicaciones.filter(id_categoria=id_categoria)

    # Obtener comentarios para cada publicación
    for publicacion in publicaciones:
        publicacion.comentarios = Comentario.objects.filter(
            id_entidad=publicacion.id_publicacion,
            tipo_entidad='publicacion'
        )

    context = {
        'publicaciones': publicaciones,
        'categorias': categorias,
        'selected_categoria': int(id_categoria) if id_categoria.isdigit() else '',
        'usuario': usuario,
        'tipo_entidad': 'publicacion',  # Se especifica el tipo de entidad como "publicacion"
    }

    return render(request, 'app_publicacion/publicaciones.html', context)



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
def crear_comentario(request, tipo_entidad, id_entidad):
    usuario_id = request.session.get('id_usuario')
    usuario = Usuario.objects.get(id_usuario=usuario_id) if usuario_id else None
    
    if not usuario:
        return HttpResponse("Debes iniciar sesión para comentar.", status=403)

    # Obtener la entidad dependiendo del tipo
    if tipo_entidad == 'convocatoria':
        entidad = get_object_or_404(Convocatoria, pk=id_entidad)
    elif tipo_entidad == 'producto':
        entidad = get_object_or_404(Producto, pk=id_entidad)
    elif tipo_entidad == 'publicacion':
        entidad = get_object_or_404(Publicacion, pk=id_entidad)
    else:
        return HttpResponse("Tipo de entidad no válido.", status=400)

    # Procesar el formulario de comentario
    if request.method == 'POST':
        texto = request.POST.get('texto')
        
        # Crear el comentario
        Comentario.objects.create(
            id_usuario=usuario,
            tipo_entidad=tipo_entidad,
            id_entidad=id_entidad,
            texto=texto
        )
        
        # Redireccionar a la página anterior
        return redirect(request.META.get('HTTP_REFERER', 'publicaciones'))

    return HttpResponse("Método no permitido", status=405)
