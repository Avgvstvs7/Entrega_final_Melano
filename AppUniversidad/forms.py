from django import forms
from django.core.exceptions import ValidationError
from .models import Profesor, Alumno


class Curso_formulario(forms.Form):
    nombre = forms.CharField(max_length=30)

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if any(char.isdigit() for char in nombre):
            raise ValidationError('El nombre no puede contener números')
        return nombre

    camada = forms.IntegerField()
    

class Profesor(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = ['profesor_id', 'curso_id']

class Alumno(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ['alumno_id', 'curso_id']
