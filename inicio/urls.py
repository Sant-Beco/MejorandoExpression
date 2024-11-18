from django.urls import path
from . import views as v

urlpatterns = [
    path('', v.ini, name='inicio'),
    path('', v.publicaciones, name='publicaciones'),
    path('producto/like/<str:tipo_entidad>/<int:id_entidad>/', v.like, name='like'),
    path('crear_comentario/<str:tipo_entidad>/<int:id_entidad>/', v.crear_comentario, name='crear_comentario'),
]
