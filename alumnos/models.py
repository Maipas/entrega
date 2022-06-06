from django.db import models

# Create your models here.
class Alumno(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    nacimiento= models.IntegerField()
    edad = models.IntegerField()
    matricula = models.CharField(max_length=30, unique=True)
    active = models.BooleanField(default=True)