from django.urls import path
from docentes.views import Docentes
from docentes.views import Agregar_docente
from docentes.views import Detalle_docente
from docentes.views import Borrar_docente, Editar_docente

urlpatterns = [
    path('docentes/', Docentes.as_view(), name = 'docentes'),
    path('agregar-docente/', Agregar_docente.as_view(), name = 'agregar_docente'),
    path('detalle-docente/<int:pk>/', Detalle_docente.as_view(), name = 'detalle_docente'),
    path('borrar-docente/<int:pk>/', Borrar_docente.as_view(), name = 'borrar_docente'),
    path('editar-docente/<int:pk>/', Editar_docente.as_view(), name = 'editar_docente'),
]