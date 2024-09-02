from django import forms
from .models import Sala

class SalaForm(forms.ModelForm):
    class Meta:
        model = Sala
        fields = ['nombre_sala', 'capacidad', 'ubicacion', 'inventario_cantidad', 'estado']