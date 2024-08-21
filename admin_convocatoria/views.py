from django.shortcuts import render,redirect,get_object_or_404
from app_funcionalidad.models import Usuario,Categoria,Convocatoria


# Create your views here.

def convocatoria_admin(request):
    usuario = Usuario.objects.all()
    id_categoria = request.GET.get('categoria', '')
    categorias = Categoria.objects.all()

    # Verificar si id_categoria es una cadena que representa un entero válido
    if id_categoria.isdigit():
        categoria_id = int(id_categoria)
        convocatorias = Convocatoria.objects.filter(id_categoria=categoria_id).order_by('-id_convocatoria')
    else:
        convocatorias = Convocatoria.objects.all().order_by('-id_convocatoria')

    return render(request, 'admin_convocatoria/convocatoria_admin.html', {
        'convocatorias': convocatorias,
        'categorias': categorias,
        'selected_categoria': int(id_categoria) if id_categoria.isdigit() else '',
        'usuario': usuario
    })

def eliminar_convo(request, id_convocatoria):
    try:
        convocatoria = get_object_or_404(Convocatoria, id_convocatoria = id_convocatoria)
        convocatoria.delete()
        return redirect('convocatoria_admin')
    except:
        return redirect('convocatoria_admin')