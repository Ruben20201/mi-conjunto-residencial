from django import forms
from .models import EmpleadoObra

class EmpleadoObraForm(forms.ModelForm):
    class Meta:
        model = EmpleadoObra
        fields = ['nombre', 'cedula', 'arl_vigente', 'apartamento_responsable', 'fecha_inicio', 'fecha_fin', 'activo']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre completo'}),
            'cedula': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Número de cédula'}),
            'arl_vigente': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'apartamento_responsable': forms.Select(attrs={'class': 'form-control'}),
            'fecha_inicio': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'fecha_fin': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }