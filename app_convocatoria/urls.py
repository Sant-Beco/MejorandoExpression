from django.urls import path
from . import views as v

urlpatterns = [
    path('', v.convocatorias, name='convocatorias'),
    path('formulario_convo/', v.formulario_convocatoria, name='formulario_convocatoria'),
]
