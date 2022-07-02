from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from docentes.models import Docente
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

class Docentes(ListView):
    model = Docente
    template_name = 'docente.html'
    queryset = Docente.objects.filter(active = True)

class Detalle_docente(DetailView):
    model = Docente
    template_name = 'docente_detalle.html'

class Agregar_docente(LoginRequiredMixin,CreateView):
    model = Docente
    template_name = 'agregar_docente.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('detalle_docente', kwargs={'pk':self.object.pk})

class Borrar_docente(LoginRequiredMixin, DeleteView):
    model = Docente
    template_name = 'docente_borrar.html'

    def get_success_url(self):
        return reverse('docentes')

class Editar_docente(LoginRequiredMixin, UpdateView):
    model = Docente
    template_name = 'docente_editar.html'
    fields = ['nombre','apellido','nacimiento','edad']

    def get_success_url(self):
        return reverse('detalle_docente', kwargs={'pk':self.object.pk})