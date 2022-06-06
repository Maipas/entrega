from django.urls import path

from basedata.views import carreras
from basedata.views import agregar_carreras



urlpatterns = [
    path('carreras/', carreras, name = 'carreras'),
    path('agregar-carrera/', agregar_carreras, name = 'agregar_carrera'),
]