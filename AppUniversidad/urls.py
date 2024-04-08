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
    path("alta_alumno", views.alumno_formulario,),
    path("ver_alumnos", views.ver_alumnos, name= "alumnos"),
    
    #URLS PROFESORES
    path("alta_profesor", views.profesores_formulario,),
    path("ver_profesores", views.ver_profesores, name= "profesores")
]