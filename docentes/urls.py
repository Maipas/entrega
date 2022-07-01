from django.urls import path
from docentes.views import docentes
from docentes.views import agregar_docentes
from docentes.views import detalle_docente
from docentes.views import borrar_docente

urlpatterns = [
    path('docentes/', docentes, name = 'alumnos'),
    path('agregar-docente/', agregar_docentes, name = 'agregar_docente'),
    path('detalle-docente/<int:pk>/', detalle_docente, name = 'detalle_docente'),
    path('borrar-docente/<int:pk>/', borrar_docente, name = 'borrar_docente'),
]