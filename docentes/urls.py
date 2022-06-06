from django.urls import path
from docentes.views import docentes
from docentes.views import agregar_docentes

urlpatterns = [
    path('docentes/', docentes, name = 'alumnos'),
    path('agregar-docente/', agregar_docentes, name = 'agregar_docente'),
]