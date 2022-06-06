from django import forms
from docentes.models import Docente

class Docente_form(forms.ModelForm):
    class Meta:
        model = Docente
        fields = '__all__'