from django.urls import path
from . import views as v

urlpatterns = [
    path('', v.productos, name='producto'),
    path('formulario_producto/', v.formulario_producto, name='formulario_producto'),
    path('producto/like/<str:tipo_entidad>/<int:id_entidad>/', v.likeproducto, name='like'),
]