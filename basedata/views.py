from django.shortcuts import render
from django.http import HttpResponse

from basedata.models import Carrera
from basedata.forms import Carrera_form

def carreras(request):
        print(request.method)
        carreras = Carrera.objects.all()
        context = {'carreras':carreras}
        return render(request, 'carrera.html', context=context)



def agregar_carreras(request):
        if request.method == 'GET':
                formularioA = Carrera_form()
                context = {'formularioA': formularioA}
                return render(request, 'agregar_carrera.html', context=context)
        else:
                formularioA = Carrera_form(request.POST)
                if formularioA.is_valid():
                        new_carrera = Carrera.objects.create(
                                carrera = formularioA.cleaned_data['carrera'],
                                descripcion = formularioA.cleaned_data['descripcion'],
                                cantidad_de_materias = formularioA.cleaned_data['cantidad_de_materias'],
                                duracion = formularioA.cleaned_data['duracion'],
                                cantidad_de_alumnos = formularioA.cleaned_data['cantidad_de_alumnos'],
                                docente = formularioA.cleaned_data['docente'],
                                active = formularioA.cleaned_data['active'],
                        )
                        context = {'new_carrera': new_carrera}
                return render(request, 'agregar_carrera.html', context=context)
