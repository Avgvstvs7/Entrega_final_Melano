from django import forms
from django.core.exceptions import ValidationError
from .models import Curso


class Curso_formulario(forms.Form):
    nombre = forms.CharField(max_length=30)

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if any(char.isdigit() for char in nombre):
            raise ValidationError('El nombre no puede contener números')
        return nombre

    camada = forms.IntegerField()
    


class profesor_formulario_alta(forms.Form):
    profesor_id = forms.CharField(label="Profesor",max_length=30)
    curso_id = forms.ModelChoiceField(label="Curso", queryset=Curso.objects.all())

    def clean_profesor_id(self):
        profesor_id = self.cleaned_data.get('profesor_id')
        if any(char.isdigit() for char in profesor_id):
            raise ValidationError('El profesor_id no puede contener números')
        return profesor_id

        
class alumno_formulario_alta(forms.Form):
    alumno_id = forms.CharField(label="Alumno",max_length=30)
    curso_id = forms.ModelChoiceField(label="Curso", queryset=Curso.objects.all())

    def clean_alumno_id(self):
        alumno_id = self.cleaned_data.get('alumno_id')
        if any(char.isdigit() for char in alumno_id):
            raise ValidationError('El alumno_id no puede contener números')
        return alumno_id