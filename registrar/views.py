# from django.shortcuts import render, redirect
# from django.contrib import messages
# from .forms import RegistroUsuarioForm
# from django.urls import reverse
# from app_funcionalidad.models import Usuario
# from django.db.models import Q

# def registro(request):
#     if request.method == 'POST':
#         form = RegistroUsuarioForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             alias = form.cleaned_data.get('alias')
#             messages.success(request, f'se registro {alias}')
#             return redirect('login')
#     else:
#         form = RegistroUsuarioForm()
#     return render(request, 'registrar/registrar.html', {'form': form})


# def login(request):
#     if request.method == 'POST':
#         alias = request.POST.get('alias')
#         contrasenia = request.POST.get('contraseña')
#         ter_con = request.POST.get('ter_con') # obtener valor terminos
        
#         if not ter_con:
#             messages.error(request, 'Debes aceptar los términos y condiciones.')
#             return render(request, 'registrar/login.html')
        
#         try:
#             usuario = Usuario.objects.get(Q(alias=alias) & Q(contrasenia=contrasenia))
#             # Guardar el ID del usuario en la sesión
#             request.session['id_usuario'] = usuario.id_usuario
#             messages.success(request, 'Inicio de sesión exitoso.')
#             return redirect('inicio')  # ruta despues de login exitoso
        
#         except Usuario.DoesNotExist:
#             messages.error(request, 'Alias o contraseña incorrectos.')
    
#     return render(request, 'registrar/login.html')

from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from app_funcionalidad.models import Usuario
from django.db.models import Q
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.hashers import make_password # encriptar
from django.contrib.auth.hashers import check_password # login encriptado

def registro(request):
    if request.method == 'POST':
        nombres = request.POST.get('nombres')
        apellidos = request.POST.get('apellidos')
        fecha_nacimiento = request.POST.get('fecha_nacimiento')
        telefono = request.POST.get('telefono')
        gmail = request.POST.get('gmail')
        alias = request.POST.get('alias')
        contrasenia = request.POST.get('contrasenia')
        verificar_contrasenia = request.POST.get('verificarContraseña')
        foto_perfil = request.FILES.get('foto_perfil')

          # Verificar si el correo ya existe
        if Usuario.objects.filter(gmail=gmail).exists():
            messages.error(request, "Este correo electrónico ya está registrado.")
            return render(request, 'registrar/registrar.html')

        # Verificar si el alias ya existe
        if Usuario.objects.filter(alias=alias).exists():
            messages.error(request, "Este alias ya está en uso.")
            return render(request, 'registrar/registrar.html')
        
        # Encriptar la contraseña
        # contrasenia = make_password(contrasenia)

        # Crear usuario
        usuario = Usuario(
            nombres=nombres,
            apellidos=apellidos,
            fecha_nacimiento=fecha_nacimiento,
            telefono=telefono,
            gmail=gmail,
            alias=alias,
            contrasenia=contrasenia,
            foto_perfil=foto_perfil,
        )
        usuario.save()
        
        # Enviar correo
        subject = 'Registro en Cultural Expression'
        message = f'{alias}, ¡Bienvenid@ a Cultural Expression!\n\nNos emociona tenerte en nuestra red social. ¡Enhorabuena! Esperamos que nuestra información sea de gran beneficio para ti.\n\nRecuerda siempre disfrutar del proceso hacia el éxito. Estamos aquí para contribuir a ti y en nuestro municipio en el arte, la cultura y el deporte.'
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [gmail]

        send_mail(subject, message, from_email, recipient_list)

        messages.success(request, "Registro exitoso. Hemos enviado un correo de bienvenida a tu dirección.")
        return redirect('login')

    return render(request, 'registrar/registrar.html')

def login(request):
    if request.method == 'POST':
        alias = request.POST.get('alias')
        contrasenia = request.POST.get('contraseña')    
        try:
            usuario = Usuario.objects.get(Q(alias=alias) & Q(contrasenia=contrasenia))
            # Guardar el ID del usuario en la sesión
            request.session['id_usuario'] = usuario.id_usuario
            messages.success(request, 'Inicio de sesión exitoso.')
            return redirect('inicio')  # ruta despues de login exitoso
        
        except Usuario.DoesNotExist:
            messages.error(request, 'Alias o contraseña incorrectos.')
    
    return render(request, 'registrar/login.html')

# def login(request):
#     if request.method == 'POST':
#         alias = request.POST.get('alias')
#         contrasenia = request.POST.get('contraseña')
#         ter_con = request.POST.get('ter_con')  # obtener valor terminos
        
#         if not ter_con:
#             messages.error(request, 'Debes aceptar los términos y condiciones.')
#             return render(request, 'registrar/login.html')
        
#         try:
#             usuario = Usuario.objects.get(alias=alias)

#             # Verificar la contraseña
#             if check_password(contrasenia, usuario.contrasenia):
#                 request.session['usuario_id'] = usuario.id_usuario
#                 messages.success(request, 'Inicio de sesión exitoso.')
#                 return redirect('publicaciones')  # Ruta después de login exitoso
#             else:
#                 messages.error(request, 'Alias o contraseña incorrectos.')

#         except Usuario.DoesNotExist:
#             messages.error(request, 'Alias o contraseña incorrectos.')
        
#     return render(request, 'registrar/login.html')