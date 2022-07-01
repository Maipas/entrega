from django.urls import path

from carreras.views import Carreras
from carreras.views import Agregar_carrera
from carreras.views import Detalle_carrera, Borrar_carrera, Editar_carrera

urlpatterns = [
    path('carreras/', Carreras.as_view(), name = 'carreras'),
    path('agregar-carrera/', Agregar_carrera.as_view(), name = 'agregar_carrera'),
    path('detalle-carrera/<int:pk>/', Detalle_carrera.as_view(), name = 'detalle_carrera'),
    path('borrar-carrera/<int:pk>/', Borrar_carrera.as_view(), name = 'borrar_carrera'),
    path('editar-carrera/<int:pk>/', Editar_carrera.as_view(), name = 'editar_carrera'),
]