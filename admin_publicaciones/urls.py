from django.urls import path
from . import views as v


urlpatterns = [
    path('', v.publicaciones_admin, name='publicacion_admin'),
]