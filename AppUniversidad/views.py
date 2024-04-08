from django.shortcuts import render
from AppUniversidad.models import Curso
from django.http import HttpResponse
from django.template import loader
from AppUniversidad.forms import Curso_formulario
from AppUniversidad.models import Alumno
from AppUniversidad.models import Profesor






def inicio(request):
    return render( request , "padre.html")



def alta_curso(request,nombre):
    curso = Curso(nombre=nombre , camada=234512)
    curso.save()
    texto = f"Se guardo en la BD el curso: {curso.nombre} {curso.camada}"
    return HttpResponse(texto)


def ver_cursos(request):
    cursos = Curso.objects.all()
    dicc = {"cursos": cursos}
    plantilla = loader.get_template("cursos.html")
    documento = plantilla.render(dicc)
    return HttpResponse(documento)



def curso_formulario(request):

    if request.method == "POST":

        mi_formulario = Curso_formulario( request.POST )

        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            curso = Curso( nombre=datos["nombre"] , camada=datos["camada"])
            curso.save()
            return render(request , "formulario.html")


    return render(request , "formulario.html")



def buscar_curso(request):

    return render(request, "buscar_curso.html")



def buscar(request):

    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        cursos = Curso.objects.filter(nombre__icontains= nombre)
        return render( request , "resultado_busqueda.html" , {"cursos":cursos})
    else:
        return HttpResponse("Ingrese el nombre del curso")
    

def elimina_curso(request , id ):
    curso = Curso.objects.get(id=id)
    curso.delete()

    curso = Curso.objects.all()

    return render(request , "cursos.html" , {"cursos":curso})




def editar(request , id):

    curso = Curso.objects.get(id=id)

    if request.method == "POST":

        mi_formulario = Curso_formulario( request.POST )
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            curso.nombre = datos["nombre"]
            curso.camada = datos["camada"]
            curso.save()

            curso = Curso.objects.all()

            return render(request , "cursos.html" , {"cursos":curso})


        
    else:
        mi_formulario = Curso_formulario(initial={"nombre":curso.nombre , "camada":curso.camada})
    
    return render( request , "editar_curso.html" , {"mi_formulario": mi_formulario , "curso":curso})

#VIEWS ALUMNOS

def alta_alumno(request,alumno_id,curso_id):
    alumno= Alumno(alumno_id= alumno , curso_id=curso_id)
    alumno.save()
    texto = f"Se guardo en la BD el alumno: {alumno_id.alumno} {curso_id.curso}"
    return HttpResponse(texto)

def ver_alumnos(request):
    alumno = Alumno.objects.all()
    dicc = {"alumnos": alumno}
    plantilla = loader.get_template("alumno_formulario.html")
    documento = plantilla.render(dicc)
    return HttpResponse(documento)

def alumno_formulario(request):
    if request.method == "POST":
        mi_alumno_formulario = Alumno(request.POST)
        if mi_alumno_formulario.is_valid():
            datos = mi_alumno_formulario.cleaned_data
            alumno = Alumno(alumno_id=datos["alumno_id"], curso_id=datos["curso_id"])
            alumno.save()
            return render(request, "alumno_formulario.html")
    else:
        mi_alumno_formulario = Alumno()
    return render(request, "alumno_formulario.html", {'form': mi_alumno_formulario})



#VIEWS PROFESORES

def alta_profesores(request,profesor_id,curso_id):
    profesor= Profesor(profesor= profesor_id , curso_id=curso_id)
    profesor.save()
    texto = f"Se guardo en la BD el alumno: {profesor.profesor_id} {profesor.curso_id}"
    return HttpResponse(texto)

def ver_profesores(request):
    profesor = Profesor.objects.all()
    dicc = {"profesores": profesor}
    plantilla = loader.get_template("profesor_formulario.html")
    documento = plantilla.render(dicc)
    return HttpResponse(documento)

def profesores_formulario(request):
    if request.method == "POST":
        mi_profesor_formulario = Profesor(request.POST)
        if mi_profesor_formulario.is_valid():
            datos = mi_alumno_formulario.cleaned_data
            nombre = Profesor(profesor_id=datos["profesor_id"], curso_id=datos["curso_id"])
            nombre.save()
            return render(request, "profesor_formulario.html")
    else:
        mi_alumno_formulario = Profesor()
    return render(request, "profesor_formulario.html", {'form': mi_profesor_formulario})