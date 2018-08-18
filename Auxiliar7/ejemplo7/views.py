from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import Formulario
from django.core.files.storage import FileSystemStorage
from .models import Cursos,Usuarios
from django.contrib.auth.models import User


def index(request):
	bienvenida={'titulo': 'Auxiliar 7','intro': 'Hoy veremos como usar formularios con bases de datos '}
	return render(request, 'ejemplo7/index.html', bienvenida)


def cursos(request):
	bienvenida={'titulo':'Cursos registrados', 'intro':"Nombre de los cursos rendidos al menos una vez ", 
	'cursos':Cursos.objects.values('nombre').distinct()}
	return render(request,'ejemplo7/cursos.html', bienvenida)

def users(request):
    info={'titulo':'Usuarios registrados en el sistema', 'intro':"Los siguientes usuarios están registrados en nuestra base de datos",
    'user':Usuarios.objects.all(),'user_beau':Usuarios.objects.exclude(puntaje_psu__gt=740)} # se escribe como atributo__condicion = valor_buscado # esto es del tipo where usuarios.puntaje_psu>740
    return render(request,'ejemplo7/users.html', info)

def adduser(request):
    form=Formulario()
    info={'titulo':'Agregar Usuarios', 'intro':"Registrese, Entreguenos todos sus datos aqui",'form':form} # se escribe como atributo__condicion = valor_buscado # esto es del tipo where usuarios.puntaje_psu>740
    return render(request,'ejemplo7/adduser.html', info)
   
def added(request):
	new_user=User.objects.create_user(username=request.POST['username'],password=request.POST['password'],email=request.POST['email'])
	new_user.save()
	usuario=Usuarios(nombre=request.POST['nombre'],apellido=request.POST['apellido'],
		direccion=request.POST['direccion'], rut=request.POST['rut'], puntaje_psu=request.POST['puntaje_psu'],user=new_user);	
	usuario.save()
	context={'Titulo':'Formulario Correcto', 'comentario':'Gracias'}
	return render(request, 'ejemplo7/added.html', context)
