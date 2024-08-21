from django.shortcuts import render, get_object_or_404, redirect 
from app_funcionalidad.models import Publicacion,Categoria,Usuario
 
def publicaciones_admin(request):
    usuario = Usuario.objects.all()
    id_categoria = request.GET.get('categoria', '')
    categorias = Categoria.objects.all()

    if id_categoria:
        publicaciones = Publicacion.objects.filter(id_categoria=id_categoria).order_by('-id_publicacion')
    else:
        publicaciones = Publicacion.objects.all().order_by('-id_publicacion')

    return render(request, 'admin_publicaciones/publicaciones_admin.html', {
        'publicaciones': publicaciones,
        'categorias': categorias,
        'selected_categoria': int(id_categoria) if id_categoria else '',
        'usuario': usuario
    })

def eliminar_publi(request, id_publicacion):
    try:
        publicacion = get_object_or_404(Publicacion, id_publicacion = id_publicacion)
        publicacion.delete()
        return redirect('publicacion_admin')
    except:
        return redirect('publicacion_admin')
   