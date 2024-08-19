from django.urls import path
from . import views as v

urlpatterns = [
    path('', v.registro, name='registrar'),
     path('login/', v.login, name='login'),
]