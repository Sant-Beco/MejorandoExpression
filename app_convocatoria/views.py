from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views.decorators.http import require_POST
from datetime import date
from app_funcionalidad.models import Usuario,Categoria,Convocatoria,Likes
from registrar.decorators import login_required_custom

@login_required_custom
def convocatorias(request):
    usuario_id = request.session.get('id_usuario')  # Asume que tienes el ID del usuario en la sesión
    usuario = Usuario.objects.get(id_usuario=usuario_id) if usuario_id else None
    id_categoria = request.GET.get('categoria', '')
    categorias = Categoria.objects.all()

    # Verificar si id_categoria es una cadena que representa un entero válido
    if id_categoria.isdigit():
        categoria_id = int(id_categoria)
        convocatorias = Convocatoria.objects.filter(id_categoria=categoria_id).order_by('-id_convocatoria')
    else:
        convocatorias = Convocatoria.objects.all().order_by('-id_convocatoria')

    return render(request, 'app_convocatoria/convocatorias.html', {
        'convocatorias': convocatorias,
        'categorias': categorias,
        'selected_categoria': int(id_categoria) if id_categoria.isdigit() else '',
        'usuario': usuario
    })


def formulario_convocatoria(request):
    if request.method == 'POST':
        titulo = request.POST['titulo']
        descripcion = request.POST['descripcion']
        fecha_inicio = request.POST['fecha_inicio']
        fecha_fin = request.POST['fecha_fin']
        lugar = request.POST['lugar']
        foto = request.FILES.get('foto')
        categoria_id = int(request.POST['categorias'])

        usuario_id = request.session.get('id_usuario')  # O el método que estás usando para obtener el ID

        try:
            # Obtener la instancia del usuario correspondiente
            usuario = Usuario.objects.get(id_usuario=usuario_id)
        except Usuario.DoesNotExist:
            return HttpResponse("Usuario no encontrado", status=404)

        convocatoria = Convocatoria(
            id_usuario=usuario,
            id_categoria_id=categoria_id,
            titulo=titulo,
            descripcion=descripcion,
            fecha_inicio=fecha_inicio,
            fecha_fin=fecha_fin,
            lugar=lugar,
            foto=foto,
            fecha_convocatoria=date.today(),
        )
        convocatoria.save()
        return redirect('convocatorias')  # Redirige a la vista de convocatorias después de guardar

    categorias = Categoria.objects.all()
    return render(request, 'app_convocatoria/formulario_convocatoria.html', {'categorias': categorias})


@require_POST
def like(request, tipo_entidad, id_entidad):
    usuario_id = request.session.get('id_usuario')  # O el método que estás usando para obtener el ID
    usuario = Usuario.objects.get(id_usuario=usuario_id)
    if tipo_entidad == 'convocatoira':
        entidad = get_object_or_404(Convocatoria, pk=id_entidad)
    if Likes.objects.filter(id_usuario=usuario, tipo_entidad=tipo_entidad, id_entidad=id_entidad).exists():      # Verificar si el usuario ya ha dado "like" a esta entidad
        return HttpResponse("Ya has dado like a esta entidad.", status=400)
    Likes.objects.create(id_usuario=usuario, tipo_entidad=tipo_entidad, id_entidad=id_entidad)

    # Redireccionar a la página anterior
    return redirect(request.META.get('HTTP_REFERER', 'convocatorias'))