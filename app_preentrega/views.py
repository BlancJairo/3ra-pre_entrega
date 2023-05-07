from django.shortcuts import render
from django.http import HttpResponse

def lista_autos(request):
    contexto = {
        "autos": [
            {"marca": "Volkswagen", "modelo": "gol", "ano":2005},
            {"marca": "Ford", "modelo": "focus", "ano":2015},
            {"marca": "chevrolet", "modelo": "corsa", "ano":2001},
        ]
    }
    http_response = render(
        request = request,
        template_name = 'pre_entrega/lista_autos.html',
        context = contexto,
    )
    return http_response