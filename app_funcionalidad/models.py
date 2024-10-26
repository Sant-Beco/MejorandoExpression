from django.db import models

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)


    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nombre_categoria = models.CharField(max_length=20)
    
    def __str__(self):
        return self.nombre_categoria

    class Meta:
        managed = False
        db_table = 'categoria'


class Convocatoria(models.Model):
    id_convocatoria = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE, db_column='id_usuario')
    id_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, db_column='id_categoria')
    titulo = models.CharField(max_length=100, blank=True, null=True)
    descripcion = models.CharField(max_length=800, blank=True, null=True)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    lugar = models.CharField(max_length=50)
    foto = models.ImageField(upload_to='foto_convo/', null=True, blank=True)
    fecha_convocatoria = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.titulo
    
    def get_likes_count(self):
        return Likes.objects.filter(tipo_entidad='convocatoria', id_entidad=self.id_convocatoria).count()

    class Meta:
        managed = False
        db_table = 'convocatoria'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE, db_column='id_usuario')
    id_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, db_column='id_categoria')
    nombre_producto = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=800)
    precio = models.IntegerField()
    archivo_multimedia = models.ImageField(upload_to='foto_produ/', null=True, blank=True)
    fecha_producto = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nombre_producto
    
    def get_likes_count(self):
        return Likes.objects.filter(tipo_entidad='producto', id_entidad=self.id_producto).count()

    class Meta:
        managed = False
        db_table = 'producto'


class Publicacion(models.Model):
    id_publicacion = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE, db_column='id_usuario')
    id_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, db_column='id_categoria')
    titulo = models.CharField(max_length=100, blank=True, null=True)
    descripcion = models.CharField(max_length=800, blank=True, null=True)
    foto = models.ImageField(upload_to='foto_publi/', null=True, blank=True)
    fecha_publicacion = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.titulo
    
    def get_likes_count(self):
        return Likes.objects.filter(tipo_entidad='publicacion', id_entidad=self.id_publicacion).count()


    class Meta:
        managed = True
        db_table = 'publicacion'


class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=40)
    apellidos = models.CharField(max_length=40)
    fecha_nacimiento = models.DateField()
    telefono = models.CharField(max_length=10, blank=True, null=True)
    gmail = models.CharField(unique=True, max_length=40)
    alias = models.CharField(unique=True, max_length=25)
    contrasenia = models.CharField(max_length=20)
    foto_perfil = models.ImageField(upload_to='fotos_perfil/', null=True, blank=True)
    rol = models.CharField(max_length=20, default='user')

    
    def __str__(self):
        return self.alias
    
    class Meta:
        managed = True
        db_table = 'usuario'

        
        
class Likes(models.Model):
    id_like = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE, db_column='id_usuario')
    tipo_entidad = models.CharField(max_length=12)
    id_entidad = models.IntegerField()
    fecha_like = models.DateField(auto_now_add=True)
    
    class Meta:
        unique_together = ('id_usuario', 'tipo_entidad', 'id_entidad')  # Garantiza unicidad

    def __str__(self):
        return f"Like by {self.id_usuario} on {self.tipo_entidad} {self.id_entidad}"

    class Meta:
        managed = False
        db_table = 'likes'

class Comentario(models.Model):
    id_comentario = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE, db_column='id_usuario')
    tipo_entidad = models.CharField(max_length=12)  # Ej: 'convocatoria', 'producto', 'publicacion'
    id_entidad = models.IntegerField()  # ID de la entidad relacionada (Convocatoria, Producto, o Publicacion)
    texto = models.TextField(max_length=800)  # Contenido del comentario
    fecha_comentario = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('id_usuario', 'tipo_entidad', 'id_entidad', 'fecha_comentario')  # Unicidad por usuario y entidad
        managed = True
        db_table = 'comentario'

    def __str__(self):
        return f"Comentario de {self.id_usuario} en {self.tipo_entidad} {self.id_entidad}"
