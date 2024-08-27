from django.urls import path
from .views import *

urlpatterns = [
    path('login_admin/', login_view, name='login_admin'),
    path('logout/', logout_view, name='logout_admin'),
]
