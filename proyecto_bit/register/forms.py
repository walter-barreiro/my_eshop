from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'}), label="Contraseña")
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Repetir contraseña'}), label="Repetir contraseña")


    class Meta:
        model = User
        fields = ["email", "username", "password1", "password2"]

        labels = {
            "email": "Diceccion de correo electronico",
            "username": "Nombre de usuario"
        }

        widgets = {
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Usuario'}),
            # 'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            # 'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }