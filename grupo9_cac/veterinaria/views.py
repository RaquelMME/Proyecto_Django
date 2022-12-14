from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render
from .models import Paciente, Familia


def pacientes(request):
    pacientes = Paciente.objects.all()
    return render(request, "veterinaria/pacientes.html", {'pacientes': pacientes})

# Creación de las vistas
def index(request):
    #template = loader.get_template('veterinaria/index.html')
    #context = {"hoy":datetime.now}
    #return HttpResponse(template.render(context,request,)
    return render(request,'veterinaria/index.html', {"hoy": datetime.now}) #la funcion render(Request, ubicación desde la carpeta template, contexto)

def contacto(request):
    #template = loader.get_template('veterinaria/index.html')
    #context = {"hoy":datetime.now}
    #return HttpResponse(template.render(context,request,)
    return render(request,'veterinaria/contacto.html')

def nosotros(request):
    #template = loader.get_template('veterinaria/index.html')
    #context = {"hoy":datetime.now}
    #return HttpResponse(template.render(context,request,)
    return render(request,'veterinaria/nosotros.html')

def admin(request):
    return render(request, 'admin')