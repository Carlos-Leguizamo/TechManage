from django import forms
from .models import Sala
from .models import Computadores

class SalaForm(forms.ModelForm):
    class Meta:
        model = Sala
        fields = ['nombre_sala', 'capacidad', 'ubicacion', 'inventario_cantidad', 'estado']

class ComputadoresForm(forms.ModelForm):
    class Meta:
        model = Computadores
        fields = ['tipo', 'marca', 'modelo', 'estado', 'fecha_adquisicion', 'id_sala']
        widgets = {
            'id_sala': forms.Select(),
        }