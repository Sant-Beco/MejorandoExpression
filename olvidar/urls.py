from django.urls import path
from .import views as v

urlpatterns = [
    path('enviar/', v.EnviarMensaje.as_view(), name='enviar'),
    path('resta/<str:id_usuario>/<slug:token>/', v.resta, name='resta'),
]
