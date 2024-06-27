from django.contrib import admin
from .models import Administrador, Profesor, Alumno, Curso, Precio

# Register your models here.

class AdministradorAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_administrador', 'nombre', 'apellidos', 'telefono', 'email', 'foto', 'creado', 'modificado')


class ProfesorAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_profesor', 'nombre', 'apellidos', 'descripcion', 'email', 'direccion', 'foto', 'creado', 'modificado')


class AlumnoAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_alumno', 'nombre', 'apellidos', 'email', 'direccion', 'foto', 'creado', 'modificado')


class CursoAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_curso', 'nombre', 'descripcion', 'imagen_curso',)
    # list_filter = ('profesor',)
    search_fields = ('nombre', 'descripcion')
    
class PrecioAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_precio', 'cantidad', 'descripcion', 'curso', 'creado', 'modificado')


admin.site.register(Administrador, AdministradorAdmin)
admin.site.register(Profesor, ProfesorAdmin)
admin.site.register(Alumno, AlumnoAdmin)
admin.site.register(Curso, CursoAdmin)
admin.site.register(Precio, PrecioAdmin)
