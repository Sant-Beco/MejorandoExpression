from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from datetime import date
from django.views.decorators.http import require_POST
from app_funcionalidad.models import Usuario, Producto, Categoria,Likes,Comentario,Convocatoria,Publicacion
from registrar.decorators import login_required_custom

@login_required_custom
def productos(request):
    productos = Producto.objects.all()
    usuario_id = request.session.get('id_usuario')
    usuario = Usuario.objects.get(id_usuario=usuario_id) if usuario_id else None
    id_categoria = request.GET.get('categoria', '')
    categorias = Categoria.objects.all()

    # Filtrado de productos por categoría
    if id_categoria.isdigit():
        productos = Producto.objects.filter(id_categoria=int(id_categoria)).order_by('-id_producto')
    else:
        productos = Producto.objects.all().order_by('-id_producto')

    # Agregar comentarios para cada producto
    for producto in productos:
        producto.comentarios = Comentario.objects.filter(id_entidad=producto.id_producto, tipo_entidad='producto')

    context = {
        'productos': productos,
        'categorias': categorias,
        'selected_categoria': int(id_categoria) if id_categoria.isdigit() else '',
        'usuario': usuario,
        'tipo_entidad': 'producto',
    }
    
    return render(request, 'app_producto/productos.html', context)



    # return render(request, 'app_producto/productos.html', {
    #     'productos': productos,
    #     'categorias': categorias,
    #     'selected_categoria': int(id_categoria) if id_categoria.isdigit() else '',
    #     'usuario': usuario
    # })

# def productos(request):
#   usuario_id = request.session.get('id_usuario')  # Asume que tienes el ID del usuario en la sesión
#   usuario = Usuario.objects.get(id_usuario=usuario_id) if usuario_id else None
#   ver = Producto.objects.all().order_by('-id_producto')
#   return render(request, 'app_producto/productos.html', {'ver':ver , 'usuario':usuario})



# def productos(request):
#     id_categoria = request.GET.get('categoria', 'all')
#     categorias = Categoria.objects.all()

#     if id_categoria == 'all':
#         productos = Producto.objects.all()
#     else:
#         productos = Producto.objects.filter(id_categoria=int(id_categoria))

#     return render(request, 'app_producto/productos.html', {
#         'productos': productos,
#         'categorias': categorias,
#         'selected_categoria': int(id_categoria) if id_categoria != 'all' else ''
#     })



def formulario_producto(request):
  if request.method == 'POST':
        nombre_producto = request.POST['nombre_producto']
        descripcion = request.POST['descripcion']
        precio = request.POST['precio']
        archivo_multimedia = request.FILES.get('archivo_multimedia')
        categoria_id = int(request.POST['categorias'])

        usuario_id = request.session.get('id_usuario')  # O el método que estás usando para obtener el ID

        try:
            # Obtener la instancia del usuario correspondiente
            usuario = Usuario.objects.get(id_usuario=usuario_id)
        except Usuario.DoesNotExist:
            return HttpResponse("Usuario no encontrado", status=404)

        producto = Producto(
            id_usuario=usuario,
            id_categoria_id=categoria_id,
            nombre_producto=nombre_producto,
            descripcion=descripcion,
            precio=precio,
            archivo_multimedia=archivo_multimedia,
            fecha_producto=date.today(),
        )
        producto.save()
        return redirect('producto')
  categorias = Categoria.objects.all()
  return render(request, 'app_producto/formulario_producto.html', {'categorias':categorias})



@require_POST
def likeproducto(request, tipo_entidad, id_entidad):
    usuario_id = request.session.get('id_usuario')
    usuario = Usuario.objects.get(id_usuario=usuario_id)
    if tipo_entidad == 'producto':
        entidad = get_object_or_404(Producto, pk=id_entidad)
    # Verificar si el usuario ya ha dado "like" a esta entidad
    if Likes.objects.filter(id_usuario=usuario, tipo_entidad=tipo_entidad, id_entidad=id_entidad).exists():
        # Opcional: puedes enviar un mensaje al usuario indicando que ya ha dado like
        return HttpResponse("Ya has dado like a esta entidad.", status=400)
    Likes.objects.create(id_usuario=usuario, tipo_entidad=tipo_entidad, id_entidad=id_entidad)

    # Redireccionar a la página anterior
    return redirect(request.META.get('HTTP_REFERER', 'producto'))


# comentarios

def crear_comentario(request, tipo_entidad, id_entidad):
    usuario_id = request.session.get('id_usuario')
    usuario = Usuario.objects.get(id_usuario=usuario_id)

    if tipo_entidad == 'convocatoria':
        entidad = get_object_or_404(Convocatoria, pk=id_entidad)
    elif tipo_entidad == 'producto':
        entidad = get_object_or_404(Producto, pk=id_entidad)
    elif tipo_entidad == 'publicacion':
        entidad = get_object_or_404(Publicacion, pk=id_entidad)
    else:
        return HttpResponse("Tipo de entidad no válido.", status=400)

    if request.method == 'POST':
        texto = request.POST.get('texto')
        Comentario.objects.create(
            id_usuario=usuario,
            tipo_entidad=tipo_entidad,
            id_entidad=id_entidad,
            texto=texto
        )
        return redirect(request.META.get('HTTP_REFERER', 'producto'))

    return HttpResponse("Método no permitido", status=405)



# def crear_comentario(request, tipo_entidad, id_entidad):
#     usuario_id = request.session.get('id_usuario')  # Obtenemos el ID del usuario desde la sesión
#     usuario = Usuario.objects.get(id_usuario=usuario_id)
    
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
#         return redirect(request.META.get('HTTP_REFERER', 'producto'))

#     return HttpResponse("Método no permitido", status=405)