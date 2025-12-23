from django import forms
from tienda_app.models import *

class TiposDeProductosForm(forms.ModelForm):
    class Meta:
        model = TiposDeProductos
        fields = [
            "tipo",
            "identificador",
        ]
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'identificador': forms.NumberInput(attrs={'class': 'form-control'}),
            'fecha_de_actualizacion': forms.DateTimeInput(attrs={'class': 'form-control'})
        }

class AnillosForm(forms.ModelForm):
    class Meta:
        model = Anillos
        fields = [
            "nombre",
            "numero",
            "unidades",
            "precio",
        ]
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'numero': forms.NumberInput(attrs={'class': 'form-control'}),
            'unidades': forms.NumberInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'fecha_de_actualizacion': forms.DateInput(attrs={'class': 'form-control'})
        }

class PulserasForm(forms.ModelForm):
    class Meta:
        model = Pulseras
        fields = [
            "nombre",
            "numero",
            "unidades",
            "precio",
        ]
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'numero': forms.NumberInput(attrs={'class': 'form-control'}),
            'unidades': forms.NumberInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'fecha_de_actualizacion': forms.DateInput(attrs={'class': 'form-control'})
        }

class CollaresForm(forms.ModelForm):
    class Meta:
        model = Collares
        fields = [
            "nombre",
            "numero",
            "unidades",
            "precio",
        ]
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'numero': forms.NumberInput(attrs={'class': 'form-control'}),
            'unidades': forms.NumberInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'fecha_de_actualizacion': forms.DateInput(attrs={'class': 'form-control'})
        }

class CombinadosForm(forms.ModelForm):
    class Meta:
        model = Combinados
        fields = [
            "nombre",
            "numero",
            "unidades",
            "precio",
        ]
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'numero': forms.NumberInput(attrs={'class': 'form-control'}),
            'unidades': forms.NumberInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'fecha_de_actualizacion': forms.DateInput(attrs={'class': 'form-control'})
        }

class CaballerosForm(forms.ModelForm):
    class Meta:
        model = Caballeros
        fields = [
            "nombre",
            "numero",
            "unidades",
            "precio",
        ]
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'numero': forms.NumberInput(attrs={'class': 'form-control'}),
            'unidades': forms.NumberInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'fecha_de_actualizacion': forms.DateInput(attrs={'class': 'form-control'})
        }

class AretesForm(forms.ModelForm):
    class Meta:
        model = Aretes
        fields = [
            "nombre",
            "numero",
            "unidades",
            "precio",
        ]
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'numero': forms.NumberInput(attrs={'class': 'form-control'}),
            'unidades': forms.NumberInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'fecha_de_actualizacion': forms.DateInput(attrs={'class': 'form-control'})
        }