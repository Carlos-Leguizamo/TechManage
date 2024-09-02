from django import forms
from .models import Sala
from .models import Computadores

class SalaForm(forms.ModelForm):
    class Meta:
        model = Sala
        fields = ['nombre_sala', 'capacidad', 'ubicacion', 'inventario_cantidad', 'estado']

class ComputadorForm(forms.ModelForm):
    class Meta:
        model = Computadores
        fields = ['id_sala', 'tipo', 'marca', 'modelo', 'numero_serie', 'fecha_adquisicion', 'estado']