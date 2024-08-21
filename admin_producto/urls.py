from django.urls import path
from . import views as v

urlpatterns = [
    path('', v.producto_admin, name='producto_admin'),
    path('eliminar_produ/<int:id_producto>/', v.eliminar_produ, name='eliminar_produ'),
]
