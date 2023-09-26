from django.urls import path
from AppUser.views import *

urlpatterns = [
    path('', inicio, name="Inicio"),
    path('Inicio/', inicio, name="Inicio"),
    path('Login/', login, name="Login"),
    path('Registro/', registro, name="Registro"),
    path('Contacto/', contacto, name="Contacto"),
    path('Articulos/', eShop, name="eshop"),
    path('Servicios/', servicios, name="servicios"),
    path('ShopSearch/', shopSearch, name="BusquedaArt"),
    path('Resultado/', resSerch, name="ResuntadosBusquedaArt"),
]
