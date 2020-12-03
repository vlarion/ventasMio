from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages 
from django.urls import reverse

from .models import Comuna,Tabla_test1,Tabla_test
from .models import Persona

def PersonaListado(request):
    persona = Persona.objects.all()
    print("Mis Registros",persona)
    return render(request, 'mantenedor/Persona/index.html', {'ParRegistros': persona}
        )
def PersonaFrm(request):
    return render(request,"mantenedor/Persona/FrPersona.html")



def ComunaFrm(request):
    return render(request,"mantenedor/Comuna/FrComuna.html")

def ComunaListado(request):
    comuna = Comuna.objects.all()
    print(comuna)
    return render(request, 'mantenedor/Comuna/index.html', {'comunaRegistros': comuna}
        )

##*************************************************
# Llamamos a la clase 'comuna' que se encuentra en nuestro archivo 'models.py'
class ComunaListado1(ListView): 
    model = Comuna 

class ComunaCrear(SuccessMessageMixin, CreateView): 
    model = Comuna # Llamamos a la clase 'Postres' que se encuentra en nuestro archivo 'models.py'
    form = Comuna # Definimos nuestro formulario con el nombre de la clase o modelo 'comuna'
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'Comuna' de nuestra Base de Datos 
    success_message = 'Comuna Creado Correctamente !' # Mostramos este Mensaje luego de Crear un Postre
 
    # Redireccionamos a la página principal luego de crear un registro o comuna
    def get_success_url(self):        
        return reverse('leer') # Redireccionamos a la vista principal 'leer'    

class ComunaDetalle(DetailView): 
    model = Comuna # Llamamos a la clase 'Comuna' que se encuentra en nuestro archivo 'models.py'

class ComunaActualizar(SuccessMessageMixin, UpdateView): 
    model = Comuna # Llamamos a la clase 'Postres' que se encuentra en nuestro archivo 'models.py' 
    form = Comuna # Definimos nuestro formulario con el nombre de la clase o modelo 'Postres' 
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Comuna Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
 
    # Redireccionamos a la página principal luego de actualizar un registro o postre
    def get_success_url(self):               
        return reverse('leer') # Redireccionamos a la vista principal 'leer'


class ComunaEliminar(SuccessMessageMixin, DeleteView): 
    model = Comuna 
    form = Comuna
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Comuna Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('leer') # Redireccionamos a la vista principal 'leer'        
##*************************************************



def index(request):
    return render(request,"mantenedor/index.html")

def producto(request):
    return render(request,"mantenedor/Productos/FrProducto.html")
def marca(request):
    return render(request,"mantenedor/Productos/FrMarca.html")
def modelo(request):
    return render(request,"mantenedor/Productos/FrModelo.html")
def bus(request):
    return render(request,"mantenedor/Productos/FrBus.html")    

def indexHarrys(request):
    return HttpResponse("Harrisito El Magnifico, Doble Magnifico")

def detail(request, preNro):
    return HttpResponse("You're looking at question SIiIII %s." % preNro)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def detailError(request, question_id):
    #question = get_object_or_404(Question, pk=question_id)
    #return render(request, 'polls/detail.html', {'question': question})    
    return render(request, 'detail.html')    