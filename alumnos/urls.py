from django.urls import path

from alumnos.views import alumnos
from alumnos.views import agregar_alumnos
from alumnos.views import detalle_alumno

urlpatterns = [
    path('alumnos/', alumnos, name = 'alumnos'),
    path('agregar-alumno/', agregar_alumnos, name = 'agregar_alumno'),
    path('detalle-alumno/<int:pk>/', detalle_alumno, name = 'detalle_alumno'),
]