from django import forms
from .models import Reportes

class ReporteForm(forms.ModelForm):
    class Meta:
        model = Reportes
        fields = ['nombre_reporte', 'id_computador', 'descripcion', 'tecnico_responsable']
        widgets = {
            'nombre_reporte': forms.TextInput(attrs={'class': 'form-control'}),
            'id_computador': forms.Select(attrs={'class': 'form-select'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 6, 'id': 'descripcion'}),
            'tecnico_responsable': forms.TextInput(attrs={'class': 'form-control'}),
        }
