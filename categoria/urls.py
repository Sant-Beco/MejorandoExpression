from django.urls import path
from . import views

urlpatterns = [
    path('', views.categoria_create, name='categoria_create'),
    path('list/', views.categoria_list, name='categoria_list'),
    path('edit/<int:pk>/', views.categoria_update, name='categoria_update'),
    path('delete/<int:pk>/', views.categoria_delete, name='categoria_delete'),
]
