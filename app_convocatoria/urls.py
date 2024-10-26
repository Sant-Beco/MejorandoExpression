from django.urls import path
from . import views as v

urlpatterns = [
    path('', v.convocatorias, name='convocatorias'),
    path('formulario_convo/', v.formulario_convocatoria, name='formulario_convocatoria'),
    path('crear_comentario/<str:tipo_entidad>/<int:id_entidad>/', v.crear_comentario, name='crear_comentario'),
]
