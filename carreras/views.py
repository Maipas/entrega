from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from carreras.models import Carrera
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

class Carreras(ListView):
        model = Carrera
        template_name = 'carrera.html'
        queryset = Carrera.objects.filter(active = True)

class Detalle_carrera(DetailView):
        model = Carrera
        template_name = 'carrera_detalle.html'

class Agregar_carrera(CreateView):
        model = Carrera
        template_name = 'agregar_carrera.html'
        fields = '__all__'

        def get_success_url(self):
                return reverse('detalle_carrera', kwargs={'pk':self.object.pk})

class Borrar_carrera(DeleteView):
        model = Carrera
        template_name = 'carrera_borrar.html'

        def get_success_url(self):
                return reverse('carreras')

class Editar_carrera(UpdateView):
        model = Carrera
        template_name = 'carrera_editar.html'
        fields = ['descripcion', 'cantidad_de_materias', 'duracion','cantidad_de_alumnos', 'docente']

        def get_success_url(self):
                return reverse('detalle_carrera', kwargs={'pk':self.object.pk})