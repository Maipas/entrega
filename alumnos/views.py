from email import message
from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from alumnos.models import Alumno
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

class Alumnos(ListView):
    model = Alumno
    template_name = 'alumno.html'
    queryset = Alumno.objects.filter(active = True)

class Detalle_alumno(DetailView):
    model = Alumno
    template_name = 'alumno_detalle.html'

class Agregar_alumno(LoginRequiredMixin, CreateView):
    model = Alumno
    template_name = 'agregar_alumno.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('detalle_alumno', kwargs={'pk':self.object.pk})

class Borrar_alumno(LoginRequiredMixin, DeleteView):
    model = Alumno
    template_name = 'alumno_borrar.html'

    def get_success_url(self):
        return reverse('alumnos')

class Editar_alumno(LoginRequiredMixin, UpdateView):
    model = Alumno
    template_name = 'alumno_editar.html'
    fields = ['nombre','apellido','nacimiento','edad']

    def get_success_url(self):
        return reverse('detalle_alumno', kwargs={'pk':self.object.pk})