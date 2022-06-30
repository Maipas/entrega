from pydoc import Doc
from django.contrib import admin
from docentes.models import Docente

@admin.register(Docente)
class DocenteAdmin(admin.ModelAdmin):
    list_display = ['apellido','nombre','nacimiento','edad','materia', 'active']