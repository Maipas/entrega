from django.contrib import admin
from alumnos.models import Alumno

@admin.register(Alumno)
class AlumnoAdmin(admin.ModelAdmin):
    list_display = ['apellido' ,'nombre', 'nacimiento','edad','matricula', 'active']