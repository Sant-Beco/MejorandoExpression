from django import forms
from app_funcionalidad.models import Usuario
from django.core.mail import send_mail
from django.conf import settings

class RegistroUsuarioForm(forms.ModelForm):
    contrasenia1 = forms.CharField(widget=forms.PasswordInput, label='Contraseña', required=True)
    contrasenia2 = forms.CharField(widget=forms.PasswordInput, label='Confirmar Contraseña', required=True)

    class Meta:
        model = Usuario
        fields = ['nombres', 'apellidos', 'fecha_nacimiento', 'telefono', 'gmail', 'alias', 'foto_perfil']

    def clean(self):
        cleaned_data = super().clean()
        contrasenia1 = cleaned_data.get("contrasenia1")
        contrasenia2 = cleaned_data.get("contrasenia2")

        if contrasenia1 and contrasenia2 and contrasenia1 != contrasenia2:
            raise forms.ValidationError("Las contraseñas no coinciden.")
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.contrasenia = self.cleaned_data["contrasenia1"]
        if commit:
            user.save()
            # Enviar correo
            subject = 'Registro en Cultural'
            message = f'{user.alias} ¡Bienvenid@ a Cultural Expression!\n \n Nos emociona que tenerte en nuestra red social !En hora buena¡ Esperamos que nuestra informacion sea de gran beneficio para ti.\n \nRecuerda siempre disfrutar del proceso hacia el exito estamos aqui para contribuir a ti y en nuestro municipio en el arte, la cultural y el deporte.'
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [user.gmail]
            send_mail(subject, message, from_email, recipient_list)
        return user

