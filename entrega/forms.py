from dataclasses import field
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class User_registration_form(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label = 'Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label = 'Repita la contraseña', widget=forms.PasswordInput)
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)

    class Meta:
        model = User
        fields = ['username','email','nombre', 'apellido', 'password1', 'password2',]
        help_texts = {k:''for k in fields}
