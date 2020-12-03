from django.shortcuts import render
from django.http import HttpResponse, StreamingHttpResponse
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages 
from django.urls import reverse
from .models import Comuna,Producto
from .models import Persona, Marca, Modelo, Proveedor
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers

#******************************  DEFINICIONES  **************************************

#******************************  PRODUCTOS  *****************************************
@csrf_exempt
def ProductoLeer(request):
    code =request.POST.get('Codigo')
    producto=Producto.objects.filter(idProducto=code)
    return StreamingHttpResponse(serializers.serialize("json", producto))

@csrf_exempt
def ProductoMirar(request):    
    code =request.POST.get('Codigo')    
    #producto=Producto.objects.filter(idProducto=code)
    producto = Producto.objects.all()
    marca = Marca.objects.all()
    modelo = Modelo.objects.all()
    proveedor = Proveedor.objects.all()
    return render(request, 'mantenedor/Productos/FrProducto.html',{'ParRegistros': producto
                                                                    , 'ParMarca': marca
                                                                    , 'ParModelo': modelo
                                                                    , 'ParProv': proveedor})

@csrf_exempt
def ProductoEliminar(request):
    idProd = request.POST.get('Codigo')
    producto = Producto.objects.get(pk=idProd)
    producto.delete()
    return StreamingHttpResponse('{"ok":"true","msg":"Producto eliminado con éxito"}')
    #return StreamingHttpResponse(serializers.serialize("json", producto))

@csrf_exempt
def ProductoActualizar(request):
    idProd = request.POST.get('Codigo')
    producto = Producto.objects.get(pk=idProd)
    producto.nombreProd = request.POST.get('Nombre')
    producto.precio = request.POST.get('Precio')
    producto.estado = request.POST.get('Estado')
    producto.garantia = request.POST.get('Garantia')
    producto.cantidad = request.POST.get('Cantidad')
    producto.fichaTecnica = request.POST.get('Ficha')
    producto.descripcion = request.POST.get('Descripcion')
    producto.imgProducto = request.POST.get('ImgProducto')
    producto.save()
    return StreamingHttpResponse('{"ok":"true","msg":"Producto actualizado con éxito"}')
    #return StreamingHttpResponse(serializers.serialize("json", producto))

@csrf_exempt
def ProductoCrear(request):
    producto = Producto.objects.all()
    print("aca vamos")

@csrf_exempt
def ProductoListado(request):
    producto = Producto.objects.all()
    marca = Marca.objects.all()
    modelo = Modelo.objects.all()
    proveedor = Proveedor.objects.all()
    return render(request, 'mantenedor/Productos/listaProd.html', {'ParRegistros': producto
                                                                   , 'ParMarca': marca
                                                                   , 'ParModelo': modelo
                                                                   , 'ParProv': proveedor})

@csrf_exempt
def ProdListado(request):
    if request.method == 'POST':        
        idProd = request.POST.get('idProducto')
        print("alerta", idProd)
        producto = Producto.objects.get(pk=idProd)        
        print("post", producto) 
    else:
        print("ELSE views")
        producto = None
    marca = Marca.objects.all()
    modelo = Modelo.objects.all()
    proveedor = Proveedor.objects.all()        
    return render(request, 'mantenedor/Productos/FrProducto.html',{'ParRegistros': producto
                                                                   , 'ParMarca': marca
                                                                   , 'ParModelo': modelo
                                                                   , 'ParProv': proveedor})

@csrf_exempt
def ProdList(request):
    if request.method == 'POST':        
        idProd = request.POST.get('Codigo')
        producto = Producto.objects.get(pk=idProd)        
    else:
        producto = None    
    marca = Marca.objects.all()
    modelo = Modelo.objects.all()
    proveedor = Proveedor.objects.all()    
    return render(request, 'mantenedor/Productos/FrProducto.html',{'ParRegistros': producto
                                                                   , 'ParMarca': marca
                                                                   , 'ParModelo': modelo
                                                                   , 'ParProv': proveedor})


@csrf_exempt
def ProdCombo(request):    
    idProv = request.POST.get('idProv')
    marca = Marca.objects.get(pk=idProv)
    return render(request, 'mantenedor/Productos/FrProducto.html',{'ParMarca': marca
                                                                   , 'ParModelo': modelo
                                                                   , 'ParProv': proveedor})


@csrf_exempt    
def ProveedorCombo(request):
    idProv =  request.POST.get('idProv')
    proveedor = Proveedor.objects.filter(idProv=idProv)
    return render(request,"mantenedor/Productos/FrProveedorCombo.html"
                         ,  {'regProveedor': proveedor}
                )
        

#******************************  PERSONAS  *****************************************

def PersonaListado(request):
    persona = Persona.objects.all()
    print("Mis Registros",persona)
    return render(request, 'mantenedor/Persona/index.html', {'DuoRegistros': persona}
        )
def PersonaFrm(request):
    return render(request,"mantenedor/Persona/FrPersona.html")


#******************************    COMUNA   *****************************************

def ComunaFrm(request):
    return render(request,"mantenedor/Comuna/FrComuna.html")

def ComunaListado(request):
    comuna = Comuna.objects.all()
    print(comuna)
    return render(request, 'mantenedor/Comuna/index.html', {'comunaRegistros': comuna}
        )

def ComunaCrear(request):
    comuna = Comuna.objects.all()
    return render(request,"mantenedor/Comuna/crear.html")

#******************************    CLASES   **********************
#******************************  PRODUCTOS  *****************************************
class ProductoDetalle(DetailView): 
    model = Producto

#******************************  COMUNA  *****************************************

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

#******************************  OTROS  *****************************************

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

#***********************  IMAGENES   ************************************

def Imagen(request):
    producto = Producto.objects.all()    
    return render(request, 'mantenedor/Productos/galeria.html', {'ImgReg': producto})

    
