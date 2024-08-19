from django import forms
from app_funcionalidad.models import Categoria

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre_categoria']
