from django.shortcuts import redirect
from functools import wraps

def login_required_custom(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if 'id_usuario' not in request.session:
            return redirect('login')  # Redirigir a la página de login si no está autenticado
        return view_func(request, *args, **kwargs)
    
    return wrapper
