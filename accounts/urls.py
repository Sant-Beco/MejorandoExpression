from django.urls import path
from .views import login_view

urlpatterns = [
    path('login_admin/', login_view, name='login_admin'),
]
