from django.shortcuts import render, redirect
from .forms import *
# importamos la clase View
from django.views import View
from .models import *

# Create your views here.
class AlumnoView(View):
    
    def get(self,request):
        listaAlumnos = TblAlumno.objects.all()
        formAlumno = AlumnoForm()
        context = {
            'alumnos' : listaAlumnos,
            'formAlumno': formAlumno
        }
        return render(request,'index.html',context)

    def post(self, request):
        formAlumno = AlumnoForm(request.POST)
        if formAlumno.is_valid():
            formAlumno.save()
            return redirect('/')
        
def Delete(request, alumno_id):
    deleteAlumnos = TblAlumno.objects.get(pk=alumno_id)
    deleteAlumnos.delete()
    return redirect('/')

def updateForm(request, alumno_id):
    updateAlumnos = TblAlumno.objects.get(pk=alumno_id)
    context = {
        'updateAlumnos' : updateAlumnos
    }
    return render(request, 'formUpdate.html', context)

def update(request, alumno_id):
    nombre = request.POST['nombre']
    email = request.POST['email']
    TblAlumno.objects.filter(pk=alumno_id).update(alumno_nombre=nombre, alumno_email=email)
    return redirect('/')

class ProfesorView(View):
    def get(self,request):
        listaProfesores = TblProfesor.objects.all()
        formProfesor = ProfesorForm()
        context = {
            'profesores' : listaProfesores,
            'formProfesor': formProfesor
        }
        return render(request,'profesor.html',context)
    
    def post(self,request):
        formProfesor = ProfesorForm(request.POST)
        if formProfesor.is_valid():
            formProfesor.save()
            return redirect('web:profesor')

def DeleteProfesor(request, profesor_id):
    deleteProfesores = TblProfesor.objects.get(pk=profesor_id)
    deleteProfesores.delete()
    return redirect('web:profesor')

def updateFormProfesor(request, profesor_id):
    updateProfesor = TblProfesor.objects.get(pk=profesor_id)
    context = {
        'updateProfesor' : updateProfesor
    }
    return render(request, 'formUpdateProfesor.html', context)

def updateProfesor(request, profesor_id):
    nombre = request.POST['nombre']
    email = request.POST['email']
    TblProfesor.objects.filter(pk=profesor_id).update(profesor_nombre=nombre, profesor_email=email)
    return redirect('/profesor')

class IndexView(View):
    def get(self,request):
        return render(request,'home.html')




