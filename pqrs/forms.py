import re
from django import forms
from django.core.exceptions import ValidationError
from .models import PQRS

# Forms par el manejo de los patterns del campo de la descripcion de la PQRS

class PQRSForm(forms.ModelForm):
    descripcion = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'required': 'required',
            'minlength': '30',
            'maxlength': '500',
            'placeholder': 'Escriba aquí los detalles de su solicitud...',
            'style': 'resize: none; overflow: hidden; height: 100px; min-height: 100px;'
        })
    )

    class Meta:
        model = PQRS
        fields = ['tipo', 'descripcion']


# Validacion dentro del formulario para la cuestion de caracteres especiales o no validos
    def clean_descripcion(self):
        descripcion = self.cleaned_data.get('descripcion')
        if not re.match(r'^[A-Za-z\s.,!?]+$', descripcion):
            raise ValidationError("La descripción solo puede contener letras, espacios, comas, puntos, signos de exclamación e interrogación.")
        return descripcion
