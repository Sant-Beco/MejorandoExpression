from django.urls import path
from . import views as v


urlpatterns = [
    path('', v.base, name='base'),
    path('base_admin/', v.base_admin, name='base_admin'),
]