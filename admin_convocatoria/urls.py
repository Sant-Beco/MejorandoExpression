from django.urls import path
from . import views as v

urlpatterns = [
    path('', v.convocatoria_admin, name='convocatoria_admin'),
    path('eliminar_convo/<int:id_convocatoria>/', v.eliminar_convo, name='eliminar_convo'),
]
