from django.urls import path

from carreras.views import carreras
from carreras.views import agregar_carreras
from carreras.views import detalle_carrera



urlpatterns = [
    path('carreras/', carreras, name = 'carreras'),
    path('agregar-carrera/', agregar_carreras, name = 'agregar_carrera'),
    path('detalle-carrera/<int:pk>/', detalle_carrera, name = 'detalle_carrera'),
]