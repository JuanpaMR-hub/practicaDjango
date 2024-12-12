from django import forms
from . import models



class PersonaForm(forms.ModelForm):
    class Meta:
        model = models.Persona
        fields = ['nombre','edad']

        labels = {
            'nombre': '',
            'edad':''
        }

        widgets={
            'nombre': forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre'}),
            'edad': forms.NumberInput(attrs={'class':'form-control','placeholder':'Edad'})
        }