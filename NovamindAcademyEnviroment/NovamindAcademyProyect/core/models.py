from django.db import models
from django.contrib.auth.models import User, AbstractUser
import uuid

# Create your models here.

class Administrador(models.Model):
    id_administrador = models.UUIDField(unique=True, auto_created=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    telefono = models.CharField(verbose_name='Teléfono', max_length=12, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    direccion = models.CharField(verbose_name='Dirección', max_length=200)
    foto = models.ImageField(verbose_name='Foto de perfil del administrador', blank=True, null=True, upload_to='perfiles')
    
    blame_user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuario culpable de guardar los datos del nuevo administrador')

    creado = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación del administrador')
    modificado = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación del administrador')
    
    class Meta:
        ordering = ('-creado', 'apellidos', 'nombre')
        verbose_name_plural = 'Administradores'

    def __str__(self) -> str:
        return f'{self.nombre}'
    

class Profesor(models.Model):
    id_profesor = models.UUIDField(unique=True, auto_created=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=100)
    descripcion = models.TextField(verbose_name='Descripción', blank=True, null=True)
    fecha_nacimiento = models.DateField()
    telefono = models.CharField(verbose_name='Teléfono', max_length=12, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    direccion = models.CharField(verbose_name='Dirección', max_length=200)
    foto = models.ImageField(verbose_name='Foto de perfil del profesor', blank=True, null=True, upload_to='perfiles')

    blame_user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuario culpable de guardar los datos del nuevo profesor')

    creado = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación del profesor')
    modificado = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación del profesor')
    
    class Meta:
        ordering = ('-creado', 'apellidos', 'nombre')
        verbose_name_plural = 'Profesores'

    def __str__(self) -> str:
        return f'{self.nombre}'


class Alumno(models.Model):
    id_alumno = models.UUIDField(unique=True, auto_created=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    telefono = models.CharField(verbose_name='Teléfono', max_length=12, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    direccion = models.CharField(verbose_name='Dirección', max_length=200)
    foto = models.ImageField(verbose_name='Foto de perfil del alumno', blank=True, null=True, upload_to='perfiles')
    
    cursos = models.ManyToManyField('Curso', verbose_name='Cursos', related_name='alumnos', blank=True)

    blame_user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuario culpable de guardar los datos del nuevo alumno')

    creado = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación del alumno')
    modificado = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación del alumno')
    
    class Meta:
        ordering = ('-creado', 'apellidos', 'nombre')

    def __str__(self) -> str:
        return f'{self.nombre}'


class Curso(models.Model):
    id_curso = models.UUIDField(unique=True, auto_created=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(verbose_name='Descripción', blank=True, null=True)
    imagen_curso = models.ImageField(verbose_name='Imagen del curso', blank=True, null=True, upload_to='img-cursos')

    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE, verbose_name='Profesor', related_name='cursos')

    blame_user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuario culpable de guardar los datos del nuevo curso')

    creado = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación del curso')
    modificado = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación del curso')

    class Meta:
        ordering = ('-creado', 'nombre',)

    def __str__(self) -> str:
        return f'{self.nombre}'
    
    def numero_alumnos_inscritos(self):
        return self.alumnos.count()

    
class Precio(models.Model):
    id_precio = models.UUIDField(unique=True, auto_created=True, default=uuid.uuid4, editable=False)
    cantidad = models.IntegerField()
    descripcion = models.TextField(verbose_name='Descripción', blank=True, null=True)
    
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name='Curso', related_name='precios')

    blame_user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuario culpable de guardar los datos del nuevo precio')
    
    creado = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación del precio')
    modificado = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación del precio')

    class Meta:
        ordering = ('-creado', 'cantidad')

    def __str__(self) -> str:
        return f'{self.cantidad}'


# class Usuario(models.Model):
    # __ADMINISTRADOR__ = 'admin'
    # __PROFESOR__ = 'profesor'
    # __ALUMNO__ = 'alumno'
    # __UNKNOWN__ = 'unknown'

    # __ROLES__ = [
    #     (__ADMINISTRADOR__, 'Administrador'),
    #     (__PROFESOR__, 'Profesor'),
    #     (__ALUMNO__, 'Alumno'),
    # ]

    # __BASE_ADMIN__ = 'base'
    # __STAFF_ADMIN__ = 'staff'

    # __ADMIN_ROLES__ = [
    #     (__BASE_ADMIN__, 'Base'),
    #     (__STAFF_ADMIN__, 'Staff'),
    # ]

    #                   #
    # DATOS DEL USUARIO #
    # id_usuario = models.UUIDField(unique=True, auto_created=True, default=uuid.uuid4, editable=False)
    # administrador = models.OneToOneField(Administrador, on_delete=models.CASCADE)
    # profesor = models.OneToOneField(Profesor, on_delete=models.CASCADE)
    # alumno = models.OneToOneField(Alumno, on_delete=models.CASCADE)
    
    #  #
    #  #
    # role = models.CharField(max_length=20, choices=__ROLES__, default=__UNKNOWN__)
    # admin_role = models.CharField(max_length=5, choices=__ADMIN_ROLES__, default=__BASE_ADMIN__)
    # blame_user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuario culpable de guardar los datos del nuevo usuario')

    #                                  #
    # DATOS DE CREACIÓN Y MODIFICACIÓN #
    # creado = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación del usuario')
    # modificado = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación del usuario')


    # class Meta:
    #     ordering = ('-creado', 'apellidos', 'nombre')

    # def __str__(self) -> str:
    #     return f'{self.nombre}'

