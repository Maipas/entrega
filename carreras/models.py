from django.db import models

# Create your models here.
class Carrera(models.Model):
    carrera = models.CharField(max_length=90, unique=True )
    descripcion = models.CharField(max_length=90)
    cantidad_de_materias= models.IntegerField()
    duracion = models.CharField(max_length=30)
    cantidad_de_alumnos = models.CharField(max_length=30)
    docente = models.CharField(max_length=30)
    active = models.BooleanField(default=True)







class Contacto(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    mail = models.CharField(max_length=120)
    consulta = models.CharField(max_length=120)
    active = models.BooleanField(default=True)