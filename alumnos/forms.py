from django import forms
from alumnos.models import Alumno

class Alumno_form(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = '__all__'