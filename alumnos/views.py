from django.shortcuts import render
from django.http import HttpResponse

from alumnos.models import Alumno
from alumnos.forms import Alumno_form

def alumnos(request):
        print(request.method)
        alumnos = Alumno.objects.all()
        context = {'alumnos': alumnos}
        return render(request, 'alumno.html', context = context)

def detalle_alumno(request, pk):
    try:
        alumno = Alumno.objects.get(id=pk)
        context = {'alumno':alumno}
        return render(request, 'alumno_detalle.html', context=context)
    except:
        context = {'error':'El alumno no existe'}
        return render(request, 'alumno.html', context=context)

def borrar_alumno(request, pk):
    try:
        if request.method == 'GET':
            alumno = Alumno.objects.get(id=pk)
            context = {'alumno':alumno}
        else:
            alumno = Alumno.objects.get(id=pk)
            alumno.delete()
            context = {'message' : 'Alumno eliminado correctamente'}

        return render(request, 'alumno_borrar.html', context = context)

    except:
        context = {'error':'El alumno no existe'}
        return render(request, 'alumno_borrar.html', context=context)

def agregar_alumnos(request):
    if request.method == 'GET':
        formularioB = Alumno_form()
        context = {'formularioB': formularioB}
        return render(request, 'agregar_alumno.html', context=context)
    else:
        formularioB = Alumno_form(request.POST)
        if formularioB.is_valid():
            new_alumno = Alumno.objects.create(
                nombre = formularioB.cleaned_data['nombre'],
                apellido = formularioB.cleaned_data['apellido'],
                nacimiento = formularioB.cleaned_data['nacimiento'],
                edad = formularioB.cleaned_data['edad'],
                matricula = formularioB.cleaned_data['matricula'],
                active = formularioB.cleaned_data['active'],
            )
            context = {'new_alumno': new_alumno}
        else:
            context = {'errors': formularioB.errors}
        return render(request, 'agregar_alumno.html', context=context)