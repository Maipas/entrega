from datetime import datetime
from genericpath import exists
from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import redirect, render
from carreras.models import Contacto
from alumnos.models import Alumno
from carreras.models import Carrera
from docentes.models import Docente
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login,logout


def login_view(request):

        if request.method == 'POST':
                form = AuthenticationForm(request, data = request.POST)

                if form.is_valid():
                        username = form.cleaned_data['username']
                        password = form.cleaned_data['password']
                        user = authenticate(username=username, password=password)

                        if user is not None:
                                login(request, user)
                                context = {'message':f'Bienvenido {username}'}
                                return render(request,'index.html', context=context)
                        else:
                                context = {'errors':'no existe ningun usuario con esas credenciales'}
                                form = AuthenticationForm()
                                return render(request, 'auth/login.html', context = context)
                else:
                        errors = form.errors
                        form=AuthenticationForm()
                        context = {'errors':errors, 'form':form}
                        return render(request, 'auth/login.html', context = context)

        else:
                form = AuthenticationForm()
                context = {'form':form}
                return render(request, 'auth/login.html', context = context)

def logout_view(request):
        logout(request)
        return redirect('index')

def index(request):
        print(request.user)
        print(request.user.is_authenticated)
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