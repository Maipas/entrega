from django.shortcuts import render
from django.http import HttpResponse

from carreras.models import Carrera
from carreras.forms import Carrera_form

def carreras(request):
        print(request.method)
        carreras = Carrera.objects.all()
        context = {'carreras':carreras}
        return render(request, 'carrera.html', context=context)

def detalle_carrera(request,pk):
        try:
                carrera = Carrera.objects.get(id=pk)
                context = {'carrera':carrera}
                return render(request, 'carrera_detalle.html', context=context)
        except:
                context = {'error':'La carrera no existe'}
                return render(request, 'carrera.html', context=context)

def borrar_carrera(request, pk):
        try:
                if request.method == 'GET':
                        carrera = Carrera.objects.get(id=pk)
                        context = {'carrera':carrera}
                else:
                        carrera = Carrera.objects.get(id=pk)
                        carrera.delete()
                        context = {'message' : 'Carrera eliminado correctamente'}

                return render(request, 'carrera_borrar.html', context = context)

        except:
                context = {'error':'La carrera no existe'}
                return render(request, 'carrera_borrar.html', context=context)

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
                else:
                        context = {'errors': formularioA.errors}
                return render(request, 'agregar_carrera.html', context=context)
