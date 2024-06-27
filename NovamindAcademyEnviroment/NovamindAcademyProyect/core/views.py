# -*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import View, TemplateView, ListView, CreateView, UpdateView, DeleteView, DetailView
from django.shortcuts import get_object_or_404
from .models import Administrador, Profesor, Alumno, Curso, Precio
import csv
from django.http import HttpResponse, HttpRequest
from typing import Any

# Create your views here.

__all__ = [
    'Inicio',
    'ListadoCursos',
    'ListadoProfesores',
    'ListadoAlumnos',
    'ListadoPrecios',
    'ListadoAlumnosPorCurso',
    'DetallesCurso',
    'DetallesProfesor',
    'Contacto',
    'SobreNosotros',
    
    'crearAdministrador',
    'borrarAdministrador',
    'modificarAdministrador',

    'crearProfesor',
    'borrarProfesor',
    'modificarProfesor',

    'crearAlumno',
    'borrarAlumno',
    'modificarAlumno',

    'crearCurso',
    'borrarCurso',
    'modificarCurso',

    'crearPrecio',
    'borrarPrecio',
    'modificarPrecio',
    
    'generarCursosCSV',
    'generarProfesoresCSV',
    'generarAlumnosCSV'
]

class Inicio(TemplateView):
    template_name = 'core/index.html'

class ListadoCursos(ListView):
    model = Curso

class ListadoProfesores(ListView):
    model = Profesor
    
class ListadoAlumnos(ListView):
    model = Alumno

class ListadoPrecios(ListView):
    model = Precio

class ListadoAlumnosPorCurso(ListView):
    model = Alumno
    template_name = 'alumno_list.html'
    context_object_name = 'alumnos'

    def get_queryset(self):
        self.curso = get_object_or_404(Curso, id_curso=self.kwargs['id'])
        return self.curso.alumnos.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['curso'] = self.curso
        return context

class DetallesCurso(DetailView):
    model = Curso
    
    def get_object(self):
        return Curso.objects.get(id_curso=self.kwargs['id'])

class DetallesProfesor(DetailView):
    model = Profesor
    
    def get_object(self):
        return Profesor.objects.get(id_profesor=self.kwargs['id'])
    

class Contacto(TemplateView):
    template_name = 'core/contact.html'
    
class SobreNosotros(TemplateView):
    template_name = 'core/aboutUs.html'



@method_decorator(login_required, name='dispatch')
class crearAdministrador(CreateView):
    model = Administrador
    fields = ('nombre', 'apellidos', 'fecha_nacimiento', 'telefono', 'email', 'direccion', 'foto',)
    success_url = reverse_lazy('administradores')

    def form_valid(self, form):
        form.instance.blame_user = self.request.user
        return super(crearAdministrador).form_valid(form)


@method_decorator(login_required, name='dispatch')
class borrarAdministrador(DeleteView):
    model = Administrador
    success_url = reverse_lazy('administradores')

    def get_object(self):
        return Administrador.objects.get(id_administrador=self.kwargs['id'])

    def dispatch(self, request, *args, **kwargs):
        administrador = self.get_object()
        if administrador.blame_user != request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


@method_decorator(login_required, name='dispatch')
class modificarAdministrador(UpdateView):
    model = Administrador
    fields = ('nombre', 'apellidos', 'fecha_nacimiento', 'telefono', 'email', 'direccion', 'foto',)
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('administradores')
    
    def get_object(self):
        return Administrador.objects.get(id_administrador=self.kwargs['id'])

    def dispatch(self, request, *args, **kwargs):
        administrador = self.get_object()
        if administrador.blame_user != request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


@method_decorator(login_required, name='dispatch')
class crearProfesor(CreateView):
    model = Profesor
    fields = ('nombre', 'apellidos', 'descripcion', 'fecha_nacimiento', 'telefono', 'email', 'direccion', 'foto',)
    success_url = reverse_lazy('profesores')

    def form_valid(self, form):
        form.instance.blame_user = self.request.user
        return super(crearProfesor, self).form_valid(form)


@method_decorator(login_required, name='dispatch')
class borrarProfesor(DeleteView):
    model = Profesor
    success_url = reverse_lazy('profesores')
    
    def get_object(self):
        return Profesor.objects.get(id_profesor=self.kwargs['id'])

    def dispatch(self, request, *args, **kwargs):
        profesor = self.get_object()
        if profesor.blame_user != request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


@method_decorator(login_required, name='dispatch')
class modificarProfesor(UpdateView):
    model = Profesor
    fields = ('nombre', 'apellidos', 'fecha_nacimiento', 'telefono', 'email', 'direccion', 'foto')
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('profesores')
    
    def get_object(self):
        return Profesor.objects.get(id_profesor=self.kwargs['id'])

    def dispatch(self, request, *args, **kwargs):
        profesor = self.get_object()
        if profesor.blame_user != request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


@method_decorator(login_required, name='dispatch')
class crearAlumno(CreateView):
    model = Alumno
    fields = ['nombre', 'apellidos', 'fecha_nacimiento', 'telefono', 'email', 'direccion', 'foto', 'cursos', 'blame_user']
    success_url = reverse_lazy('precios')


@method_decorator(login_required, name='dispatch')
class borrarAlumno(DeleteView):
    model = Alumno
    success_url = reverse_lazy('alumnos')
    
    def get_object(self):
        return Alumno.objects.get(id_alumno=self.kwargs['id'])

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
            Alumno = self.get_object()
            if Alumno.blame_user != request.user:
                # Lanzar una excepción
                raise PermissionDenied
            return super().dispatch(request, *args, **kwargs)

    
    

@method_decorator(login_required, name='dispatch')
class modificarAlumno(UpdateView):
    model = Alumno
    fields = ('nombre', 'apellidos', 'fecha_nacimiento', 'telefono', 'email', 'direccion', 'foto', 'cursos', 'blame_user')
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('alumnos')
    
    def get_object(self):
        return Alumno.objects.get(id_alumno=self.kwargs['id'])

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        Alumno = self.get_object()
        if Alumno.blame_user != request.user:
            raise PermissionError
        return super().dispatch(request, *args, **kwargs)
    

@method_decorator(login_required, name='dispatch')
class crearCurso(CreateView):
    model = Curso
    fields = ('nombre', 'descripcion', 'imagen_curso', 'profesor', 'blame_user')
    success_url = reverse_lazy('cursos')

    def form_valid(self, form):
        form.instance.blame_user = self.request.user
        return super(crearCurso, self).form_valid(form)
    

@method_decorator(login_required, name='dispatch')
class borrarCurso(DeleteView):
    model = Curso
    success_url = reverse_lazy('cursos')
    
    def get_object(self):
        return Curso.objects.get(id_curso=self.kwargs['id'])
    
    def dispatch(self, request, *args, **kwargs):
        curso = self.get_object()
        if curso.blame_user != request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


@method_decorator(login_required, name='dispatch')
class modificarCurso(UpdateView):
    model = Curso
    fields = ('nombre', 'descripcion', 'profesor', 'imagen_curso', 'profesor', 'blame_user')
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('cursos')
    
    def get_object(self):
        return Curso.objects.get(id_curso=self.kwargs['id'])

    def dispatch(self, request, *args, **kwargs):
        curso = self.get_object()
        if curso.blame_user != request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

@method_decorator(login_required, name='dispatch')
class crearPrecio(CreateView):
    model = Precio
    fields = ('cantidad', 'descripcion', 'curso', 'blame_user')
    success_url = reverse_lazy('precios')

    def form_valid(self, form):
        form.instance.blame_user = self.request.user
        return super(crearPrecio, self).form_valid(form)
    

@method_decorator(login_required, name='dispatch')
class borrarPrecio(DeleteView):
    model = Precio
    success_url = reverse_lazy('precios')
    
    def get_object(self):
        return Precio.objects.get(id_precio=self.kwargs['id'])
    
    def dispatch(self, request, *args, **kwargs):
        precio = self.get_object()
        if precio.blame_user != request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


@method_decorator(login_required, name='dispatch')
class modificarPrecio(UpdateView):
    model = Precio
    fields = ('nombre', 'descripcion',)
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('precios')
    
    def get_object(self):
        return Precio.objects.get(id_precio=self.kwargs['id'])

    def dispatch(self, request, *args, **kwargs):
        precio = self.get_object()
        if precio.blame_user != request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class generarCursosCSV(View):
    # Definir función para generar el archivo CSV
    def get(self, request, *args, **kwargs):
        # Crear respuesta HTTP con el tipo de contenido 'text/csv
        response = HttpResponse(content_type='text/csv')
        # Indicar el nombre que va a tener el archivo CSV generado
        response['Content-Disposition'] = 'attachment; filename="cursos.csv"'

        # Crear el escritor CSV
        writer = csv.writer(response)
        # Escribir en el fichero CSV la fila de la cabecera
        writer.writerow(['Id_Curso', 'Nombre', 'Profesor', 'Usuario Responsable', 'Fecha Creacion', 'Fecha Modificacion'])

        # Obtener todos los cursos del modelo "Curso"
        cursos = Curso.objects.all()

        # Recorrer cada uno de los cursos obtenidos
        for curso in cursos:
            # Mostrar los datos de cada uno de los cursos recorridos en el fichero CSV
            writer.writerow([curso.id_curso, curso.nombre, curso.profesor, curso.blame_user, curso.creado, curso.modificado])
        
        # Devolver la respuesta HTTP que contiene el fichero CSV
        return response
    
class generarProfesoresCSV(View):
    def get(self, request, *args, **kwargs):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="profesores.csv"'
        
        writer = csv.writer(response)
        
        # Imprimir la cabecera del fichero CSV
        writer.writerow(['Id_Profesor', 'Nombre', 'Apellidos', 'Fecha Nacimiento', 'Telefono', 'Email', 'Direccion', 'Usuario Responsable', 'Fecha Creacion', 'Fecha Modificacion'])
        
        profesores = Profesor.objects.all()
        
        for profesor in profesores:
            writer.writerow([profesor.id_profesor, profesor.nombre, profesor.apellidos, profesor.fecha_nacimiento, profesor.telefono, profesor.email, profesor.direccion, profesor.blame_user, profesor.creado, profesor.modificado])
            
        return response
    
class generarAlumnosCSV(View):
    def get(self, request, *args, **kwargs):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="alumnos.csv"'
        
        writer = csv.writer(response)
        
        # Imprimir la cabecera del fichero CSV
        writer.writerow(['Id_Alumno', 'Nombre', 'Apellidos', 'Fecha Nacimiento', 'Telefono', 'Email', 'Direccion', 'Cursos', 'Usuario Responsable', 'Fecha Creacion', 'Fecha Modificacion'])
        
        alumnos = Alumno.objects.all()
        
        for alumno in alumnos:
            writer.writerow([alumno.id_alumno, alumno.nombre, alumno.apellidos, alumno.fecha_nacimiento, alumno.telefono, alumno.email, alumno.direccion, ", ".join([curso.nombre for curso in alumno.cursos.all()]), alumno.blame_user, alumno.creado, alumno.modificado])
            
        return response