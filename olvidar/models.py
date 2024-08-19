from django.db import models

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=40)
    apellidos = models.CharField(max_length=40)
    fecha_nacimiento = models.DateField()
    telefono = models.CharField(max_length=10, blank=True, null=True)
    gmail = models.CharField(unique=True, max_length=40)
    alias = models.CharField(unique=True, max_length=25)
    contrasenia = models.CharField(max_length=20)

    rol = models.CharField(max_length=20, default='user')

    def __str__(self):
        return self.alias

    class Meta:
        managed = False
        db_table = 'usuario'

    def actualizar_contrasenia(self, nueva_contrasenia):
        self.contrasenia = nueva_contrasenia
        self.save()

        
