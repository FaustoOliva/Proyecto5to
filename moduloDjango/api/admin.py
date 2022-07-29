from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Alumno)
class AlumnoAdmin(admin.ModelAdmin):
    list_display = ['legajo', 'nombre', 'apellido', 'idcurso']

@admin.register(Aula)
class AulaAdmin(admin.ModelAdmin):
    list_display = ['idaula', 'numcamara']
    
@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ['idcurso', 'nombre']

@admin.register(Cxmxpxa)
class CxmxpxaAdmin(admin.ModelAdmin):
    list_display = ['idcmpa', 'idcurso', 'idmateria', 'bloquedia', 'idaula', 'idprofesor']

@admin.register(Materia)
class MateriaAdmin(admin.ModelAdmin):
    list_display = ['idmateria', 'nombre']

@admin.register(Presencia)
class PresenciaAdmin(admin.ModelAdmin):
    list_display = ['idpresencia', 'legajoalumno', 'idcmpa', 'fecha', 'tiempo', 'estado']

@admin.register(ProfesorA)
class ProfesorAAdmin(admin.ModelAdmin):
    list_display = ['idprofesor', 'nombre', 'apellido']
