from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from app_preentrega.models import autos, Camionetas, Camiones, motos, bicicletas

def lista_autos(request): #esto renderiza una lista con el contexto que se le pase
    contexto = { 
        "autos" : autos.objects.all()
    }
    http_response = render(
        request = request,
        template_name = 'pre_entrega/lista_autos.html',
        context = contexto,
    )
    return http_response

def lista_camionetas(request): #esto renderiza una lista con el contexto que se le pase
    contexto = { 
        "camionetas" : Camionetas.objects.all()
    }
    http_response = render(
        request = request,
        template_name = 'pre_entrega/lista_camionetas.html',
        context = contexto,
    )
    return http_response

def lista_camiones(request): #esto renderiza una lista con el contexto que se le pase
    contexto = { 
        "camiones" : Camiones.objects.all()
    }
    http_response = render(
        request = request,
        template_name = 'pre_entrega/lista_camiones.html',
        context = contexto,
    )
    return http_response

def lista_motos(request): #esto renderiza una lista con el contexto que se le pase
    contexto = { 
        "motos" : motos.objects.all()
    }
    http_response = render(
        request = request,
        template_name = 'pre_entrega/lista_motos.html',
        context = contexto,
    )
    return http_response

def lista_bicicletas(request): #esto renderiza una lista con el contexto que se le pase
    contexto = { 
        "bicicletas" : bicicletas.objects.all()
    }
    http_response = render(
        request = request,
        template_name = 'pre_entrega/lista_bicicletas.html',
        context = contexto,
    )
    return http_response

def subir_autos(request): 
    if request.method == 'POST':
        data = request.POST
        marca = data ["marca"]
        modelo = data ["modelo"]
        ano = data ["ano"]
        color = data ["color"]
        equipamiento = data ["equipamiento"]
        descripcion = data ["descripcion"]
        auto = autos(
            marca = marca,
            modelo = modelo,
            ano = ano,
            color = color,
            equipamiento = equipamiento, 
            descripcion = descripcion
        )
        auto.save()
        url_exitosa = reverse('autos')
        return redirect(url_exitosa)
    else:
        Http_response = render(
        request = request,
        template_name = 'pre_entrega/formulario_crear_auto.html', 
        )
        return Http_response
    
def subir_camionetas(request): 
    if request.method == "POST":
        data = request.POST
        marca = request ["marca"]
        modelo = request ["modelo"]
        ano = request ["ano"]
        color = request ["color"]
        equipamiento = request ["equipamiento"]
        descripcion = request ["descripcion"]
        Camionetas.objects.create(
            marca = marca,
            modelo = modelo,
            ano = ano,
            color = color,
            equipamiento = equipamiento, 
            descripcion = descripcion,
        )
        url_exitosa = reverse('camionetas')
        return redirect(url_exitosa)
    else:
        Http_response = render(
        request = request,
        template_name = 'pre_entrega/formulario_crear_camionetas.html', 
        )
        return Http_response
    
def subir_camiones(request): 
    if request.method == "POST":
        data = request.POST
        marca = request ["marca"]
        modelo = request ["modelo"]
        ano = request ["ano"]
        color = request ["color"]
        equipamiento = request ["equipamiento"]
        descripcion = request ["descripcion"]
        Camiones.objects.create(
            marca = marca,
            modelo = modelo,
            ano = ano,
            color = color,
            equipamiento = equipamiento, 
            descripcion = descripcion,
        )
        url_exitosa = reverse('camiones')
        return redirect(url_exitosa)
    else:
        Http_response = render(
        request = request,
        template_name = 'pre_entrega/formulario_crear_camiones.html', 
        )
        return Http_response
    
def subir_motos(request): 
    if request.method == "POST":
        data = request.POST
        marca = request ["marca"]
        modelo = request ["modelo"]
        ano = request ["ano"]
        color = request ["color"]
        equipamiento = request ["equipamiento"]
        descripcion = request ["descripcion"]
        motos.objects.create(
            marca = marca,
            modelo = modelo,
            ano = ano,
            color = color,
            equipamiento = equipamiento, 
            descripcion = descripcion,
        )
        url_exitosa = reverse('motos')
        return redirect(url_exitosa)
    else:
        Http_response = render(
        request = request,
        template_name = 'pre_entrega/formulario_crear_motos.html', 
        )
        return Http_response
    
def subir_bicicletas(request): 
    if request.method == "POST":
        data = request.POST
        marca = request ["marca"]
        modelo = request ["modelo"]
        ano = request ["ano"]
        color = request ["color"]
        equipamiento = request ["equipamiento"]
        descripcion = request ["descripcion"]
        bicicletas.objects.create(
            marca = marca,
            modelo = modelo,
            ano = ano,
            color = color,
            equipamiento = equipamiento, 
            descripcion = descripcion,
        )
        url_exitosa = reverse('bicicletas')
        return redirect(url_exitosa)
    else:
        Http_response = render(
        request = request,
        template_name = 'pre_entrega/formulario_crear_bicicletas.html', 
        )
        return Http_response

