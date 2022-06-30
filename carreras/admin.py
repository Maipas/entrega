from django.contrib import admin
from carreras.models import Carrera

@admin.register(Carrera)
class CarreraAdmin(admin.ModelAdmin):
    list_display = ['carrera', 'descripcion','cantidad_de_materias','duracion','cantidad_de_alumnos','docente','active']