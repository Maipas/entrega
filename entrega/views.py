from django.shortcuts import redirect, render
from alumnos.models import Alumno
from carreras.models import Carrera
from docentes.models import Docente
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login,logout
from entrega.forms import User_registration_form
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views import generic

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

def register_view(request):
        if request.method == "POST":
                form = User_registration_form(request.POST)
                if form.is_valid():
                        form.save()
                        username = form.cleaned_data['username']
                        password = form.cleaned_data['password1']
                        nombre = form.cleaned_data['nombre']
                        apellido = form.cleaned_data['apellido']
                        user = authenticate(username=username, password=password, nombre=nombre, apellido=apellido)
                        login(request, user)
                        context ={'message':f'Usuario creado correctamente. Bievenido {username}'}
                        return render(request, 'index.html', context = context)
                else:
                        errors = form.errors
                        form = User_registration_form()
                        context = {'errors':errors, 'form':form}
                        return render (request, 'auth/register.html', context = context)
        else:
                form = User_registration_form()
                context = {'form':form}
                return render(request, 'auth/register.html', context = context)

class Usereditview(generic.UpdateView):
        form_class = User_registration_form
        template_name = 'auth/edit_profile.html'
        
        def get_success_url(self):
                return reverse('index')
        
        def get_object(self):
                return self.request.user


def index(request):
        print(request.user)
        print(request.user.is_authenticated)
        # print(request.user.user_profile)
        return render(request, 'index.html')

# @login_required
# def contacto(request):
#         contacto = Contacto.objects.all()
#         context = {'contacto': contacto         }
#         return render(request, 'contacto.html', context = context)
        
def contacto(request):
        if request.user.is_authenticated:
                return render(request, 'contacto.html')
        else:
                return redirect('login')

def search(request):
        print(request.GET)
        alumnos = Alumno.objects.filter(apellido__icontains = request.GET['search'])
        carreras = Carrera.objects.filter(carrera__icontains = request.GET['search'])
        docentes = Docente.objects.filter(apellido__icontains = request.GET['search'])
        context = {'alumnos':alumnos, 'carreras':carreras, 'docentes':docentes}
        return render(request, 'search.html', context = context)
#por algunas razon no puedo hacer que busque en mas categorias
