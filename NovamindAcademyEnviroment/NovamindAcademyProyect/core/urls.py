from .views import *
from django.urls import path

urlpatterns = [
    path('', Inicio.as_view(), name='inicio'),

    # LISTADOS
    path('cursos/', ListadoCursos.as_view(), name='cursos'),    
    path('profesores/', ListadoProfesores.as_view(), name='profesores'),
    path('alumnos/', ListadoAlumnos.as_view(), name='alumnos'),
    path('precios/', ListadoPrecios.as_view(), name='precios'),
    path('alumnos/cursos/<uuid:id>', ListadoAlumnosPorCurso.as_view(), name='alumnos_por_curso'),

    # CREAR
    # path('administradores/crear/', crearAdministrador.as_view(), name='crear_administrador'),
    path('profesores/crear/', crearProfesor.as_view(), name='crear_profesor'),
    path('alumnos/crear/', crearAlumno.as_view(), name='crear_alumno'),
    path('cursos/crear/', crearCurso.as_view(), name='crear_curso'),
    path('precios/crear/', crearPrecio.as_view(), name='crear_precio'),

    # MODIFICAR
    # path('administradores/modificar/<uuid:id>', modificarAdministrador.as_view(), name='modificar_administrador'),
    path('profesores/modificar/<uuid:id>/', modificarProfesor.as_view(), name='modificar_profesor'),
    path('alumnos/modificar/<uuid:id>', modificarAlumno.as_view(), name='modificar_alumno'),
    path('cursos/modificar/<uuid:id>', modificarCurso.as_view(), name='modificar_curso'),
    path('precios/modificar/<uuid:id>', modificarPrecio.as_view(), name='modificar_precio'),

    # BORRAR
    # path('administradores/borrar/<uuid:id>', borrarAdministrador.as_view(), name='borrar_administrador'),
    path('profesores/borrar/<uuid:id>/', borrarProfesor.as_view(), name='borrar_profesor'),
    path('alumnos/borrar/<uuid:id>/', borrarAlumno.as_view(), name='borrar_alumno'),
    path('cursos/borrar/<uuid:id>/', borrarCurso.as_view(), name='borrar_curso'),
    path('precios/borrar/<uuid:id>/', borrarPrecio.as_view(), name='borrar_precio'),

    # DETALLES
    path('cursos/<uuid:id>/', DetallesCurso.as_view(), name='detalles_curso'),
    path('profesores/<uuid:id>/', DetallesProfesor.as_view(), name='detalles_profesor'),

    # OTROS
    path('sobre-nosotros/', SobreNosotros.as_view(), name='sobre-nosotros'),
    path('contacto/', Contacto.as_view(), name='contacto'),
    
    # EXPORTAR MODELOS
    path('cursos/exportar/', generarCursosCSV.as_view(), name='exportar-cursos'),
    path('profesores/exportar/', generarProfesoresCSV.as_view(), name='exportar-profesores'),
    path('alumnos/exportar', generarAlumnosCSV.as_view(), name='exportar-alumnos')
]
