from django.urls import path
from . import views as v

urlpatterns = [
    path('', v.producto_admin, name='produc'),
]
