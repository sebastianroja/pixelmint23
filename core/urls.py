from django.urls import path
from .views import *
from .form import ClientForm
from django.conf import settings
from django.conf.urls.static import static
from turtle import settiltangle

#para agregar nuevas path de url hay que agregar una coma al diccionario urlpatterns y seguir el formato descrito
urlpatterns = [
    path('index/', index,name="index"),
    path('Contacto', Contacto, name="Contacto"),
    path('', iniciarsesion, name="iniciarsesion"),
    path('productos/', productos, name="productos"),
    path('Crearcuenta/', Crearcuenta, name="Crearcuenta"),
    #path('EditarPerfil/', EditarPerfil, name="EditarPerfil"),
      path('EditarPerfil_copy/', profile, name="EditarPerfil_copy"),
    path('carritoCompras/', carritoCompras, name="carritoCompras")


]
urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)