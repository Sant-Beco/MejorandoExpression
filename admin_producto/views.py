# from django.shortcuts import render

# # Create your views here.
# def producto_admin(request):
#     return render(request, 'admin_producto/producto_admin.html')

from django.shortcuts import render, get_object_or_404, redirect
from app_funcionalidad.models import Usuario, Producto, Categoria

# Create your views here.

def producto_admin(request):
    usuario = Usuario.objects.all()
    id_categoria = request.GET.get('categoria', '')
    categorias = Categoria.objects.all()

    # Verificar si id_categoria es una cadena que representa un entero válido
    if id_categoria.isdigit():
        categoria_id = int(id_categoria)
        productos = Producto.objects.filter(id_categoria=categoria_id).order_by('-id_producto')
    else:
        productos = Producto.objects.all().order_by('-id_producto')

    return render(request, 'admin_producto/producto_admin.html', {
        'productos': productos,
        'categorias': categorias,
        'selected_categoria': int(id_categoria) if id_categoria.isdigit() else '',
        'usuario': usuario
    })
    
def eliminar_produ(request, id_producto):
    try:
        producto = get_object_or_404(Producto, id_producto = id_producto)
        producto.delete()
        return redirect('producto_admin')
    except:
        return redirect('producto_admin')