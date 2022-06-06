from django.urls import path

from alumnos.views import alumnos
from alumnos.views import agregar_alumnos

urlpatterns = [
    path('alumnos/', alumnos, name = 'alumnos'),
    path('agregar-alumno/', agregar_alumnos, name = 'agregar_alumno'),
]