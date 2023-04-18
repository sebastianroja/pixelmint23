from django.shortcuts import render, redirect
from .form import *
from .models import Producto
from .models import Usuario
from django.contrib.auth import get_user_model


# Create your views here. aca se debe crear una nueva funcion para la nueva landig

class usuario:
    def _init_(self, correo, contraseña):
        self.correo=correo
        self.contraseña=contraseña


def index(request):
    User = get_user_model()
    print(User.objects.all())
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
            User = get_user_model()
            user = User.objects.create_user(email=formulario['Correo'].value(), password="foo",username="hola")
            formulario.save()
            datos['mensaje'] = "Guardado Correctamente"
            
    return render(request,'core/Crearcuenta.html',datos)


def EditarPerfil(request):
    #traer usuario actual#
    idUsuario=1
    print (idUsuario) 
    user = Usuario.objects.get(idUsuario=idUsuario)
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