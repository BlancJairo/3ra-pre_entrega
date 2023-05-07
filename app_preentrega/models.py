from django.db import models

class Camionetas (models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    ano = models.ImageField(max_length=50)
    color = models.CharField(max_length=15)
    equipamiento = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)

class autos (models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    ano = models.ImageField(max_length=50)
    color = models.CharField(max_length=15)
    equipamiento = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)

class Camiones (models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    ano = models.ImageField(max_length=50)
    color = models.CharField(max_length=15)
    equipamiento = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)

class motos (models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    ano = models.ImageField(max_length=50)
    color = models.CharField(max_length=15)
    equipamiento = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)

class bicicletas (models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    ano = models.ImageField(max_length=50)
    color = models.CharField(max_length=15)
    equipamiento = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)
