from django import forms 
from app_funcionalidad.models import Usuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['fecha_nacimiento','gmail','alias','telefono','foto_perfil']
        widgets = {
            'fecha_nacimiento': forms.TextInput(attrs={
                'class': 'campos'
            }),
            'telefono': forms.TextInput(attrs={
                'class': 'campos'
            }),
            'gmail': forms.TextInput(attrs={
                'class': 'campos'
            }),
            'alias': forms.TextInput(attrs={
                'class': 'campos'
            }),  
            'foto_perfil': forms.ClearableFileInput(attrs={'class': 'custom-file-input'}),
        }
        
        
        
        