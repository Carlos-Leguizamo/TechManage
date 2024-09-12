from django import forms
from .models import PQRS

class PQRSForm(forms.ModelForm):
    class Meta:
        model = PQRS
        fields = ['tipo', 'descripcion']  # Incluir los campos a mostar en el formulario

    
