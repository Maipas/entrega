from django.urls import path

from carreras.views import carreras
from carreras.views import agregar_carreras



urlpatterns = [
    path('carreras/', carreras, name = 'carreras'),
    path('agregar-carrera/', agregar_carreras, name = 'agregar_carrera'),
]