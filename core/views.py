from django.shortcuts import render, redirect
from .form import *
from .models import Producto
from .models import Usuario



# Create your views here. aca se debe crear una nueva funcion para la nueva landig

class usuario:
    def _init_(self, correo, contraseña):
        self.correo=correo
        self.contraseña=contraseña


def index(request):
    return render(request, 'core/index.html')

def Contacto(request):
     return render(request, 'core/Contacto.html')


def iniciarsesion(request):
     return render(request, 'core/iniciarsesion.html')

def productos(request):
    product=Producto.objects.all()
    context= {"Products":product}
    print (context)
    return render(request, 'core/productos_copy.html',context)
def productos_copy(request):
    return render(request, 'core/productos_copy.html')

def Crearcuenta(request):
    datos = {
        'form': ClientForm()
    }
    if request.method=='POST':
        formulario= ClientForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Guardado Correctamente"
            
    return render(request,'core/Crearcuenta.html',datos)


def EditarPerfil(request, id):
    
    print (id) 
    user = Usuario.objects.get(idUsuario=id)
    print(user)
    datos = {
        'form': ClientForm(instance=user)
    }
    if request.method=='POST':
        formulario= ClientForm(data=request.POST, instance=user)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Modificado Correctamente"

    return render(request, 'core/EditarPerfil.html', datos)











def carritoCompras(request):
    return render(request, 'core/carritoCompras.html')