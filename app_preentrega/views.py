from django.shortcuts import render
from django.http import HttpResponse

def lista_autos(request): #esto renderiza una lista con el contexto que se le pase
    contexto = {  }
    http_response = render(
        request = request,
        template_name = 'pre_entrega/lista_autos.html',
        context = contexto,
    )
    return http_response

def lista_camionetas(request): #esto renderiza una lista con el contexto que se le pase
    contexto = {  }
    http_response = render(
        request = request,
        template_name = 'pre_entrega/lista_camionetas.html',
        context = contexto,
    )
    return http_response

def lista_camiones(request): #esto renderiza una lista con el contexto que se le pase
    contexto = {  }
    http_response = render(
        request = request,
        template_name = 'pre_entrega/lista_camiones.html',
        context = contexto,
    )
    return http_response

def lista_motos(request): #esto renderiza una lista con el contexto que se le pase
    contexto = {  }
    http_response = render(
        request = request,
        template_name = 'pre_entrega/lista_motos.html',
        context = contexto,
    )
    return http_response

def lista_bicicletas(request): #esto renderiza una lista con el contexto que se le pase
    contexto = {  }
    http_response = render(
        request = request,
        template_name = 'pre_entrega/lista_bicicletas.html',
        context = contexto,
    )
    return http_response