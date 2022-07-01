from django.urls import path

from alumnos.views import Alumnos
from alumnos.views import Agregar_alumno
from alumnos.views import Detalle_alumno, Borrar_alumno, Editar_alumno

urlpatterns = [
    path('alumnos/', Alumnos.as_view(), name = 'alumnos'),
    path('agregar-alumno/', Agregar_alumno.as_view(), name = 'agregar_alumno'),
    path('detalle-alumno/<int:pk>/', Detalle_alumno.as_view(), name = 'detalle_alumno'),
    path('borrar-alumno/<int:pk>/', Borrar_alumno.as_view(), name = 'borrar_alumno'),
    path('editar-alumno/<int:pk>/', Editar_alumno.as_view(), name = 'editar_alumno'),
]