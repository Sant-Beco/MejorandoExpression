from django.urls import path
from . import views as v


urlpatterns = [
    path('', v.perfil, name='perfil'),
    path('delete_publicacion/<int:id_publicacion>/',v.delete_publicacion, name='delete_publicacion'),
    path('delete_convocatoria/<int:id_convocatoria>/',v.delete_convocatoria, name='delete_convocatoria'),
    path('delete_producto/<int:id_producto>/',v.delete_producto, name='delete_producto'),
    path('update/<id_usuario>', v.update, name='update'),
    path('logout/', v.logout_usu, name='logout_usu'),
    
]