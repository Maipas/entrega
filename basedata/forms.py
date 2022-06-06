from django import forms
from basedata.models import Carrera

class Carrera_form(forms.ModelForm):
    class Meta:
        model = Carrera
        fields = '__all__'
