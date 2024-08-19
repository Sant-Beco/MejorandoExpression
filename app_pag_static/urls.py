from django.urls import path
from . import views as v

urlpatterns = [
    path('base_pag_static/', v.base_pag_static, name= 'base_pag_static'),
    path('', v.vista_principal, name= 'vista_principal'),
    path('acerca_nosotros/', v.acerca_nosotros, name='acerca_nosotros'),
    path('reglas_negocio/', v.reglas_negocio, name='reglas_negocio'),
    path('terminos_condiciones/', v.terminos_condiciones, name= 'terminos_condiciones'),
]