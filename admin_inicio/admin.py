from django.contrib import admin
from django.shortcuts import render, redirect
from django.contrib.admin.views.decorators import staff_member_required

# Register your models here.
@staff_member_required
def inicio_admin(request):
    # Aquí va la lógica para la vista del panel de administración
    return render(request, 'admin/inicio_admin.html')