from django.shortcuts import render
from app_funcionalidad.models import Publicacion, Convocatoria, Categoria, Producto
import plotly.express as px
import plotly.io as pio
import pandas as pd

def inicio_admin(request):
    # Obtener datos de publicaciones, convocatorias, productos y categorías
    publicaciones = Publicacion.objects.all()
    convocatorias = Convocatoria.objects.all()
    productos = Producto.objects.all()
    categorias = Categoria.objects.all()

    # Crear DataFrame para publicaciones por categoría
    data_publicaciones = []
    for categoria in categorias:
        cat_publicaciones = publicaciones.filter(id_categoria=categoria.id_categoria).count()
        data_publicaciones.append({
            'categoria': categoria.nombre_categoria,
            'publicaciones': cat_publicaciones
        })
    
    df_publicaciones = pd.DataFrame(data_publicaciones)
    fig_publicaciones = px.bar(df_publicaciones, x='categoria', y='publicaciones', title='Cantidad de Publicaciones por Categoría')

    # Crear DataFrame para convocatorias por categoría
    data_convocatorias = []
    for categoria in categorias:
        cat_convocatorias = convocatorias.filter(id_categoria=categoria.id_categoria).count()
        data_convocatorias.append({
            'categoria': categoria.nombre_categoria,
            'convocatorias': cat_convocatorias
        })
    
    df_convocatorias = pd.DataFrame(data_convocatorias)
    fig_convocatorias = px.bar(df_convocatorias, x='categoria', y='convocatorias', title='Cantidad de Convocatorias por Categoría')

    # Crear DataFrame para productos por categoría
    data_productos = []
    for categoria in categorias:
        cat_productos = productos.filter(id_categoria=categoria.id_categoria).count()
        data_productos.append({
            'categoria': categoria.nombre_categoria,
            'productos': cat_productos
        })
    
    df_productos = pd.DataFrame(data_productos)
    fig_productos = px.bar(df_productos, x='categoria', y='productos', title='Cantidad de Productos por Categoría')

    # Convertir las gráficas a JSON
    graph_publicaciones_json = pio.to_json(fig_publicaciones)
    graph_convocatorias_json = pio.to_json(fig_convocatorias)
    graph_productos_json = pio.to_json(fig_productos)

    context = {
        'graph_publicaciones_json': graph_publicaciones_json,
        'graph_convocatorias_json': graph_convocatorias_json,
        'graph_productos_json': graph_productos_json,
    }
    
    return render(request, 'admin_inicio/inicio_admin.html', context)

