from django.shortcuts import render

# Create your views here.
def convocatoria_admin(request):
    return render(request, 'admin_convocatoria/convocatoria_admin.html')