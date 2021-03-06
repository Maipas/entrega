from django.db import models

# Create your models here.
class Docente(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    nacimiento= models.DateField()
    edad = models.IntegerField()
    materia = models.CharField(max_length=30, unique=True)
    active = models.BooleanField(default=True)
    image=models.ImageField(upload_to ='docentes', blank=True, null=True)

    class Meta:
        verbose_name = 'docente'
        verbose_name_plural = 'docentes'