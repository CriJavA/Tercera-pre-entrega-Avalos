from django.db import models

class MainUser(models.Model):
    NickName = models.CharField(max_length=60)
    UserName = models.CharField(max_length=60)
    UserDate = models.DateField()
    UserAddress = models.CharField(max_length=60)
    UserPass = models.CharField(max_length=20)
    UserEmail = models.EmailField()
    UserTnum = models.CharField(max_length=20)
    
class Articulo(models.Model):
    Marca = models.CharField(max_length=60)
    Modelo = models.CharField(max_length=60)
    Year = models.CharField(max_length=4)
    Color = models.CharField(max_length=20)
    Precio = models.FloatField(max_length=10)
    Descrip = models.CharField(max_length=500)
    
class Service(models.Model):
    Tipo = models.CharField(max_length=30)
    Subtipo = models.CharField(max_length=30)
    Precio = models.FloatField(max_length=10)
    Descrip = models.CharField(max_length=500)
    