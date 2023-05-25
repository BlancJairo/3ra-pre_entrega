from django import forms

class Formulario (forms.Form):
    marca = forms.CharField(required=True, max_length=50)
    modelo = forms.CharField(required=True, max_length=50)
    ano = forms.IntegerField(required=True, max_value=9999)
    color = forms.CharField(required=True, max_length=15)
    equipamiento = forms.CharField(required=True, max_length=100)
    descripcion = forms.CharField(required=True, max_length=200)    