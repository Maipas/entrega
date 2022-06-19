from datetime import datetime
from genericpath import exists

from django.http import HttpResponse
from django.shortcuts import render
from carreras.models import Contacto
from alumnos.models import Alumno
from carreras.models import Carrera
from docentes.models import Docente

def index(request):
        return render(request, 'index.html')

def contacto(request):
        contacto = Contacto.objects.all()
        context = {'contacto': contacto         }
        return render(request, 'contacto.html', context = context)

def search(request):
        print(request.GET)
        alumnos = Alumno.objects.filter(nombre__contains = request.GET['search'])
        carreras = Carrera.objects.filter(carrera__contains = request.GET['search'])
        docentes = Docente.objects.filter(nombre__contains = request.GET['search'])
        context = {'alumnos':alumnos, 'carreras':carreras, 'docentes':docentes}
        return render(request, 'search.html', context = context)