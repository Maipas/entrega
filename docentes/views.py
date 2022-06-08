from django.shortcuts import render
from django.http import HttpResponse

from docentes.models import Docente
from docentes.forms import Docente_form

def docentes(request):
        print(request.method)
        docentes = Docente.objects.all()
        context = {'docentes': docentes}
        return render(request, 'docente.html', context = context)



def agregar_docentes(request):
    if request.method == 'GET':
        formularioC = Docente_form()
        context = {'formularioC': formularioC}
        return render(request, 'agregar_docente.html', context=context)
    else:
        formularioC = Docente_form(request.POST)
        if formularioC.is_valid():
            new_docente = Docente.objects.create(
                nombre = formularioC.cleaned_data['nombre'],
                apellido = formularioC.cleaned_data['apellido'],
                nacimiento = formularioC.cleaned_data['nacimiento'],
                edad = formularioC.cleaned_data['edad'],
                materia = formularioC.cleaned_data['materia'],
                active = formularioC.cleaned_data['active'],
            )
            context = {'new_docente': new_docente}
        else:
            context = {'errors': formularioC.errors}
        return render(request, 'agregar_docente.html', context=context)