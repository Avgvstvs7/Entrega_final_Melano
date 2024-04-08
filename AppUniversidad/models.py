from django.db import models

# Create your models here.


class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()
    
    def __str__(self):
        return self.nombre

class Profesor(models.Model):
    profesor_id = models.CharField(max_length=100)
    curso_id = models.ManyToManyField(Curso)

    def __str__(self):
        return self.profesor_id

class Alumno(models.Model):
    alumno_id = models.CharField(max_length=100)
    curso_id = models.ManyToManyField(Curso)

    def __str__(self):
        return self.alumno_id