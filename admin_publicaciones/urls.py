from django.urls import path
from . import views as v


urlpatterns = [
    path('', v.publicaciones_admin, name='publicacion_admin'),
    path('eliminar_publi/<int:id_publicacion>/', v.eliminar_publi, name='eliminar_publi'),
]