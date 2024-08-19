from django.shortcuts import render

# Create your views here.
def producto_admin(request):
    return render(request, 'admin_producto/producto_admin.html')
