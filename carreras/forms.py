from django import forms
from carreras.models import Carrera

class Carrera_form(forms.ModelForm):
    class Meta:
        model = Carrera
        fields = '__all__'