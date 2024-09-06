from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm

class CustomUserChangeForm(UserChangeForm):
   
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'required': 'required',
            'pattern': '^[A-Z][a-z]{1,49}(?: [A-Z][a-z]{1,49})*$',
            'title': 'El nombre debe comenzar con una letra mayúscula y solo puede contener letras y espacios. Cada palabra debe comenzar con una letra mayúscula y tener entre 2 y 50 caracteres.'
        })
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'required': 'required',
            'pattern': '^[A-Z][a-z]{1,49}(?: [A-Z][a-z]{1,49})*$',
            'title': 'El apellido debe comenzar con una letra mayúscula y solo puede contener letras y espacios. Cada palabra debe comenzar con una letra mayúscula y tener entre 2 y 50 caracteres.'
        })
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'required': 'required',
            'pattern': r'^[^@]+@[^@]+\.[a-zA-Z]{2,}$',  # Asegura que el correo tenga un '@' y un dominio.
            'title': 'Ingrese una dirección de correo electrónico válida con un "@" y un dominio.'
            
        })
    )
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
