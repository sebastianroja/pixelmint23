from django.shortcuts import render, redirect
from .form import *
from .models import Producto
from .models import Usuario
from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model
from django.contrib import messages


# Create your views here. aca se debe crear una nueva funcion para la nueva landig

class usuario:
    def _init_(self, correo, contraseña):
        self.correo = correo
        self.contraseña = contraseña


def iniciarsesion(request):
    print("holaquetal")
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print("usernotnone")
            login(request, user)
            return redirect('index')
        else:
            print('usernone')
            error_message = 'nombre de usuario o contraseña incorrecto'
            return render(request, 'core/iniciarsesion.html', {'error_message': error_message})
    return render(request, 'core/iniciarsesion.html')


def index():
    return render('core/index.html')


def index(request):
    User = get_user_model()
    print(User.objects.all())
    return render(request, 'core/index.html')


def Contacto(request):
    return render(request, 'core/Contacto.html')


# def iniciarsesion(request):
#     return render(request, 'core/iniciarsesion.html')

def productos(request):
    product = Producto.objects.all()
    context = {"Products": product}
    print(context)
    return render(request, 'core/productos_copy.html', context)


def productos_copy(request):
    return render(request, 'core/productos_copy.html')


def Crearcuenta(request):

    datos = {
        'form': ClientForm()
    }
    if request.method == 'POST':
        
        formulario = ClientForm(request.POST)
        print(formulario)
        if formulario.is_valid:
            User = get_user_model()
            #user = User.objects.create_user(email=formulario['Correo'].value(), password="foo",username="hola")
            formulario.save()
            datos['mensaje'] = "Guardado Correctamente"

    return render(request, 'core/Crearcuenta.html', datos)


def EditarPerfil(request):
    import random
    # traer usuario actual#
    idUsuario = random.randint(1, 4)
    print(idUsuario)
    user = Usuario.objects.get(idUsuario=idUsuario)
    print(user)
    datos = {
        'form': ClientForm(instance=user)
    }
    if request.method == 'POST':
        formulario = ClientForm(data=request.POST, instance=user)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Modificado Correctamente"

    return render(request, 'core/EditarPerfil.html', datos)


def profile(request):
    print("hola profile")
    user = request.user
    print(user)
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name'] 
        email = request.POST['email'] 
        user.first_name = first_name 
        user.last_name = last_name 
        user.email = email 
        user.save() 
        messages.success(request, 'Datos actualizados exitosamente')
        return redirect('index')
    return render(request, 'core/EditarPerfil_copy.html', {'user':user})


def carritoCompras(request):
    return render(request, 'core/carritoCompras.html')
