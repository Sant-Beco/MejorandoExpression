from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    #URLS DE USUARIO
    path('', include('app_pag_static.urls')),
    path('pag_static/', include('app_pag_static.urls')),
    path('inicio/', include('inicio.urls')),
    path('publicacion/', include('app_publicacion.urls')),
    path('convocarias/', include('app_convocatoria.urls')),
    path('producto/', include('app_producto.urls')),
    path('perfil/', include('app_perfil.urls')),
    path('registrar/', include('registrar.urls')),
    path('base/', include('app_funcionalidad.urls')),
    
    #URLS DE ADMINISTRADOR
    
    path('categoria/',  include('categoria.urls')),
    path('convocatoria_admin/',  include('admin_convocatoria.urls')),
    path('publicaciones_admin/',  include('admin_publicaciones.urls')),
    path('inicio_admin/',  include('admin_inicio.urls')),
    path('admin_producto/',  include('admin_producto.urls')),
    
    #APLICACIONES DE REQUERIMIENTO
    
    path('olvidar/',  include('olvidar.urls')),
    path('verificar/',  include('verificar.urls')),
    
    path('accounts/', include('accounts.urls')),
    
    
    
    
    
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)