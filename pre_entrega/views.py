from django.shortcuts import render
from django.http import HttpResponse


def inicio(request):
    contexto = {}
    http_response = render(
        request = request,
        template_name = 'pre_entrega/index.html',
        context = contexto,
    )
    return http_response

def saludo(recuest):
    return HttpResponse("Hola")

def saludar_con_html(request):
    contexto = {}
    http_response = render(
        request = request,
        template_name = 'pre_entrega/base.html',
        context = contexto,
    )
    return http_response