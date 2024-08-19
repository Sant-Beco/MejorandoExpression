from django.contrib import admin
from .models import Categoria
from .models import Convocatoria
from .models import Producto
from .models import Publicacion
from .models import Usuario

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Convocatoria)
admin.site.register(Producto)
admin.site.register(Publicacion)
admin.site.register(Usuario)