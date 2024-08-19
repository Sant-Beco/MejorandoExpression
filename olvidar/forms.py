from django import forms

class EmailForm(forms.Form):
    email = forms.EmailField(label='Correo electrónico')

class RestaForm(forms.Form):
    nueva_contrasenia = forms.CharField(label='Nueva contraseña', widget=forms.PasswordInput)
    confirmar_contrasenia = forms.CharField(label='Confirmar nueva contraseña', widget=forms.PasswordInput)
