from django import forms

class userforms(forms.Form):
    NickName = forms.CharField()
    UserName = forms.CharField()
    UserDate = forms.DateField()
    UserAddress = forms.CharField()
    UserPass = forms.CharField()
    UserEmail = forms.EmailField()
    UserTnum = forms.CharField()
    
class articuloform(forms.Form):
    Marca = forms.CharField()
    Modelo = forms.CharField()
    Year = forms.CharField()
    Color = forms.CharField()
    Precio = forms.FloatField()
    Descrip = forms.CharField()
    
class serviceform(forms.Form):
    Tipo = forms.CharField()
    Subtipo = forms.CharField()
    Precio = forms.FloatField()
    Descrip = forms.CharField()
    
class loginform(forms.Form):
    NickName = forms.CharField()
    UserAddress = forms.CharField()