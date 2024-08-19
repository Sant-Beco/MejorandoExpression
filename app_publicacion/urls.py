from django.urls import path
from . import views as v


urlpatterns = [
    path('', v.publicaciones, name='publicaciones'),
    path('formulario_publicacion/' , v.formulario_publicacion, name= "formulario_publicacion"),
    path('producto/like/<str:tipo_entidad>/<int:id_entidad>/', v.like, name='like'),
]
