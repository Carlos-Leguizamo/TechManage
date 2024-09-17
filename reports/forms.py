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
    
    def clean_descripcion(self):
        descripcion = self.cleaned_data.get('descripcion')
        if len(descripcion) < 500:
            raise forms.ValidationError("La descripción debe tener al menos 500 caracteres.")
        return descripcion
