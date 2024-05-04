from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from AppUniversidad.models import Curso
from AppUniversidad.forms import Curso_formulario
from AppUniversidad.models import Alumno
from AppUniversidad.models import Profesor
from AppUniversidad.forms import alumno_formulario_alta
from AppUniversidad.forms import profesor_formulario_alta
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm
from django.contrib.auth import login, authenticate






def inicio(request):
    return render( request , "padre.html")



# def alta_curso(request,nombre):
#     curso = Curso(nombre=nombre , camada=234512)
#     curso.save()
#     texto = f"Se guardo en la BD el curso: {curso.nombre} {curso.camada}"
#     return HttpResponse(texto)


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

def alta_alumno(request):
    if request.method == 'POST':
        form = alumno_formulario_alta(request.POST)
        if form.is_valid():
            alumno_id = form.cleaned_data.get('alumno_id')
            curso_id = form.cleaned_data.get('curso_id')
            Alumno.objects.create(alumno_id=alumno_id, curso_id=curso_id)
            return redirect('alta_alumno')
        print(form.errors)
    else:
        form = alumno_formulario_alta()
    return render(request, 'alumno_alta.html', {'form': form})



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



def elimina_alumno(request , id ):
    alumno_id = Alumno.objects.get(id=id)
    alumno_id.delete()

    alumno_id = Alumno.objects.all()

    return render(request , "alumno_formulario.html" , {"alumnos":alumno_id})




def editar_alumno(request , id):

    alumno_id = Alumno.objects.get(id=id)

    if request.method == "POST":

        mi_formulario = alumno_formulario_alta( request.POST )
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            alumno_id.alumno_id = datos["alumno_id"]
            alumno_id.curso_id = datos["curso_id"]
            alumno_id.save()

            alumno_id = Alumno.objects.all()

            return render(request , "alumno_formulario.html" , {"alumnos":alumno_id})


        
    else:
        mi_formulario = alumno_formulario_alta(initial={"alumno_id":alumno_id.alumno_id , "curso_id":alumno_id.curso_id})
    
    return render( request , "editar_alumno.html" , {"mi_formulario": mi_formulario , "alumno_id":alumno_id})

#VIEWS PROFESORES

def alta_profesor(request):
    if request.method == 'POST':
        form = profesor_formulario_alta(request.POST)
        if form.is_valid():
            profesor_id = form.cleaned_data.get('profesor_id')
            curso_id = form.cleaned_data.get('curso_id')
            Profesor.objects.create(profesor_id=profesor_id, curso_id=curso_id)
            return redirect('alta_profesor')
        print(form.errors)
    else:
        form = profesor_formulario_alta()
    return render(request, 'profesor_alta.html', {'form': form})


def ver_profesores(request):
    profesor = Profesor.objects.all()
    dicc = {"profesores": profesor}
    plantilla = loader.get_template("profesor_formulario.html")
    documento = plantilla.render(dicc)
    return HttpResponse(documento)

def profesores_formulario(request):
    if request.method == "POST":
        mi_profesor_formulario = profesor_formulario_alta(request.POST)
        if mi_profesor_formulario.is_valid():
            datos = mi_profesor_formulario.cleaned_data
            profesor = profesor_formulario_alta(profesor_id=datos["profesor_id"], curso_id=datos["curso_id"])
            profesor.save()
            return render(request, "profesor_formulario.html")
    else:
        mi_profesor_formulario = profesor_formulario_alta()
    return render(request, "profesor_formulario.html", {'form': mi_profesor_formulario})




def elimina_profesor(request , id ):
    profesor_id = Profesor.objects.get(id=id)
    profesor_id.delete()

    profesor_id = Profesor.objects.all()

    return render(request , "profesor_formulario.html" , {"profesores":profesor_id})




def editar_profesor(request , id):

    profesor_id = Profesor.objects.get(id=id)

    if request.method == "POST":

        mi_formulario = profesor_formulario_alta( request.POST )
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            profesor_id.profesor_id = datos["profesor_id"]
            profesor_id.curso_id = datos["curso_id"]
            profesor_id.save()

            profesor_id = Profesor.objects.all()

            return render(request , "profesor_formulario.html" , {"profesores": profesor_id})


        
    else:
        mi_formulario = profesor_formulario_alta(initial={"profesor_id":profesor_id.profesor_id , "curso_id":profesor_id.curso_id})
    
    return render( request , "editar_profesor.html" , {"mi_formulario": mi_formulario , "profesor_id": profesor_id})




def login_request(request):

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():

            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")

            user = authenticate(username=usuario , password=contra)

            if user is not None:
                login(request , user )
                return render( request , "inicio.html" , {"mensaje":f"Bienvenido/a {usuario}", "usuario":usuario})
            else:
                return HttpResponse(f"No se encontró el usuario")
        else: 
            return HttpResponse(f"FORM INCORRECTO {form}")


    form = AuthenticationForm()
    return render( request , "login.html" , {"form":form})




def register(request):
    
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponse("Usuario creado")

    else:
        form = UserCreationForm()
    return render(request , "registro.html" , {"form":form})
