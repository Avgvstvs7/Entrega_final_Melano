from django.urls import path
from . import views

urlpatterns = [
    #URLS CURSOS
    path("", views.inicio , name="home"),
    path("ver_cursos", views.ver_cursos , name="cursos"),
    path("alta_curso", views.curso_formulario),
    path("buscar_curso", views.buscar_curso),
    path("buscar", views.buscar),
    path("elimina_curso/<int:id>" , views.elimina_curso , name="elimina_curso"),
    path("editar_curso/<int:id>" , views.editar , name="editar_curso"),
   
    #URLS ALUMNOS
    path("alta_alumno", views.alta_alumno, name='alta_alumno'),
    path("ver_alumnos", views.ver_alumnos, name="alumnos"),
    path("elimina_alumno/<int:id>" , views.elimina_alumno , name="elimina_alumno"),
    path("editar_alumno/<int:id>" , views.editar_alumno , name="editar_alumno"),
    
    #URLS PROFESORES
    path("alta_profesor", views.alta_profesor, name='alta_profesor'),
    path("ver_profesores", views.ver_profesores, name= "profesores"),
    path("elimina_profesor/<int:id>" , views.elimina_profesor , name="elimina_profesor"),
    path("editar_profesor/<int:id>" , views.editar_profesor , name="editar_profesor")

]