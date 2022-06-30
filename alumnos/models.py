from datetime import datetime
from django.db import models

# Create your models here.
class Alumno(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    nacimiento= models.DateField()
    edad = models.IntegerField()
    matricula = models.CharField(max_length=30, unique=True)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'alumno'
        verbose_name_plural = 'alumnos'