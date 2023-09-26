from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *

#def mUser (request):
    #User1 = MainUser(NickName = "Pepe Python",
                    #UserName = "Pedro André",
                    #UserDate = "12/05/1980",
                    #UserAddress = "Calle Cabildo N° 1234",
                    #UserPass = "123456",
                    #UserEmail = "PepeP@Coder.com",
                    #UserTnum = "+54 22536885424",
                #)
    #User1.save
    
    #return HttpResponse(f"Se a creado con exito el usuario {User1.NickName}")

def inicio (request):
    return render(request, "AppUser/inicio.html")

def login (request):
    return render(request, "AppUser/login.html")

def contacto (request):
    return render(request, "AppUser/contacto.html")

def registro (request):
    if request.method == "POST":
        form_x = userforms(request.POST)
        if form_x.is_valid():
            infoA = form_x.cleaned_data
            user = MainUser(NickName=infoA["NickName"],
                            UserName=infoA["UserName"],
                            UserDate=infoA["UserDate"],
                            UserAddress=infoA["UserAddress"],
                            UserPass=infoA["UserPass"],
                            UserEmail=infoA["UserEmail"],
                            UserTnum=infoA["UserTnum"],
                            )
            user.save()
            return render(request, "AppUser/Inicio.html")
    else:
        form_x = userforms()
    return render(request, "AppUSer/userForm.html", {"formKeyA":form_x})

def eShop (request):
    if request.method == "POST":
        form_y = articuloform(request.POST)
        if form_y.is_valid():
            infoB = form_y.cleaned_data
            articulo = Articulo(Marca=infoB["Marca"],
                                    Modelo=infoB["Modelo"],
                                    Year=infoB["Year"],
                                    Color=infoB["Color"],
                                    Precio=infoB["Precio"],
                                    Descrip=infoB["Descrip"],
                                    )
            articulo.save()
            return render(request, "AppUser/Inicio.html")
    else:
        form_y = articuloform()
    return render(request, "AppUser/shop.html", {"formKeyB":form_y})

def servicios (request):
    if request.method == "POST":
        form_z = serviceform(request.POST)
        if form_z.is_valid():
            infoC = form_z.cleaned_data
            serv = Service(Tipo=infoC["Tipo"],                           
                           Subtipo=infoC["Subtipo"],           
                           Precio=infoC["Precio"],
                           Descrip=infoC["Descrip"],
                           )
            serv.save()
            return render(request, "AppUser/Inicio.html")
    else:
        form_z = serviceform()
    return render(request, "AppUser/servicios.html", {"formKeyC":form_z})

def login (request):
    pass

def shopSearch(request):
    return render(request, "AppUser/shopSearch.html")

def resSerch (request):
    
    if request.GET["Marca"]:
        marcaArt = request.GET["Marca"]
        artMarcas = Articulo.objects.filter(Marca__icontains=marcaArt)
        return render(request, "AppUser/resultado.html", {"artMarcas":artMarcas, "marcaArt":marcaArt})
    else:
        respuesta = "No ingresaste datos."
    
    return HttpResponse(respuesta)