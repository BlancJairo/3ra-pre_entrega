from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from app_preentrega.models import autos, Camionetas, Camiones, motos, bicicletas
from app_preentrega.forms import Formulario

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
        "Camionetas" : Camionetas.objects.all()
    }
    http_response = render(
        request = request,
        template_name = 'pre_entrega/lista_camionetas.html',
        context = contexto,
    )
    return http_response

def lista_camiones(request): #esto renderiza una lista con el contexto que se le pase
    contexto = { 
        "Camiones" : Camiones.objects.all()
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

#Con estas view creamos

def subir_autos(request): 
    if request.method == "POST":
        formulario = Formulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            marca = data ["marca"]
            modelo = data ["modelo"]
            ano = data ["ano"]
            color = data ["color"]
            equipamiento = data ["equipamiento"]
            descripcion = data ["descripcion"]
            vehiculo = autos(
                marca = marca,
                modelo = modelo,
                ano = ano,
                color = color,
                equipamiento = equipamiento, 
                descripcion = descripcion
            )
            vehiculo.save()
            url_exitosa = reverse('autos')
            return redirect(url_exitosa)
     
    else:
        formulario = Formulario()    
    Http_response = render(
        request = request,
        template_name = 'pre_entrega/formulario_crear_auto.html', 
        context={'formulario':formulario}
        )
    return Http_response
    
def subir_camionetas(request): 
    if request.method == "POST":
        formulario = Formulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            marca = data ["marca"]
            modelo = data ["modelo"]
            ano = data ["ano"]
            color = data ["color"]
            equipamiento = data ["equipamiento"]
            descripcion = data ["descripcion"]
            vehiculo = Camionetas(
                marca = marca,
                modelo = modelo,
                ano = ano,
                color = color,
                equipamiento = equipamiento, 
                descripcion = descripcion
            )
            vehiculo.save()
            url_exitosa = reverse('camionetas')
            return redirect(url_exitosa)
     
    else:
        formulario = Formulario()    
    Http_response = render(
        request = request,
        template_name = 'pre_entrega/formulario_crear_camionetas.html', 
        context={'formulario':formulario}
        )
    return Http_response
    
def subir_camiones(request): 
    if request.method == "POST":
        formulario = Formulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            marca = data ["marca"]
            modelo = data ["modelo"]
            ano = data ["ano"]
            color = data ["color"]
            equipamiento = data ["equipamiento"]
            descripcion = data ["descripcion"]
            vehiculo = Camiones(
                marca = marca,
                modelo = modelo,
                ano = ano,
                color = color,
                equipamiento = equipamiento, 
                descripcion = descripcion
            )
            vehiculo.save()
            url_exitosa = reverse('camiones')
            return redirect(url_exitosa)
     
    else:
        formulario = Formulario()    
    Http_response = render(
        request = request,
        template_name = 'pre_entrega/formulario_crear_camiones.html', 
        context={'formulario':formulario}
        )
    return Http_response
    
def subir_motos(request): 
    if request.method == "POST":
        formulario = Formulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            marca = data ["marca"]
            modelo = data ["modelo"]
            ano = data ["ano"]
            color = data ["color"]
            equipamiento = data ["equipamiento"]
            descripcion = data ["descripcion"]
            vehiculo = motos(
                marca = marca,
                modelo = modelo,
                ano = ano,
                color = color,
                equipamiento = equipamiento, 
                descripcion = descripcion
            )
            vehiculo.save()
            url_exitosa = reverse('motos')
            return redirect(url_exitosa)
     
    else:
        formulario = Formulario()    
    Http_response = render(
        request = request,
        template_name = 'pre_entrega/formulario_crear_motos.html', 
        context={'formulario':formulario}
        )
    return Http_response
    
def subir_bicicletas(request): 
    if request.method == "POST":
        formulario = Formulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            marca = data ["marca"]
            modelo = data ["modelo"]
            ano = data ["ano"]
            color = data ["color"]
            equipamiento = data ["equipamiento"]
            descripcion = data ["descripcion"]
            vehiculo = bicicletas(
                marca = marca,
                modelo = modelo,
                ano = ano,
                color = color,
                equipamiento = equipamiento, 
                descripcion = descripcion
            )
            vehiculo.save()
            url_exitosa = reverse('bicicletas')
            return redirect(url_exitosa)
     
    else:
        formulario = Formulario()    
    Http_response = render(
        request = request,
        template_name = 'pre_entrega/formulario_crear_bicicletas.html', 
        context={'formulario':formulario}
        )
    return Http_response
#Con estas view buscamos 

def buscar_auto (request):
    
    if request.method == "POST":
        data=request.POST
        busqueda = data["busqueda"]
        auto = autos.objects.filter(modelo__icontains=busqueda)
        contexto = { 
        "autos" : auto,
        }
    http_response = render(
        request = request,
        template_name = 'pre_entrega/lista_autos.html',
        context = contexto,
    )
    return http_response

def buscar_camionetas (request):
    
    if request.method == "POST":
        data=request.POST
        busqueda = data["busqueda"]
        camioneta = Camionetas.objects.filter(modelo__icontains=busqueda)
        contexto = { 
        "Camionetas" : camioneta,
        }
    http_response = render(
        request = request,
        template_name = 'pre_entrega/lista_camionetas.html',
        context = contexto,
    )
    return http_response

def buscar_camiones (request):
    
    if request.method == "POST":
        data=request.POST
        busqueda = data["busqueda"]
        camion = Camiones.objects.filter(modelo__icontains=busqueda)
        contexto = { 
        "Camiones" : camion,
        }
    http_response = render(
        request = request,
        template_name = 'pre_entrega/lista_camiones.html',
        context = contexto,
    )
    return http_response

def buscar_bicicletas (request):
    
    if request.method == "POST":
        data=request.POST
        busqueda = data["busqueda"]
        bici = bicicletas.objects.filter(modelo__icontains=busqueda)
        contexto = { 
        "bicicletas" : bici,
        }
    http_response = render(
        request = request,
        template_name = 'pre_entrega/lista_bicicletas.html',
        context = contexto,
    )
    return http_response

def buscar_motos (request):
        
    if request.method == "POST":
        data=request.POST
        busqueda = data["busqueda"]
        moto = motos.objects.filter(modelo__icontains=busqueda)
        contexto = { 
        "motos" : moto,
        }
    http_response = render(
        request = request,
        template_name = 'pre_entrega/lista_motos.html',
        context = contexto,
    )
    return http_response

#Con estas view eliminamos 

def eliminar_auto(request, id): 
   
    auto = autos.objects.get(id=id)
    
    if request.method == "POST":
        
        auto.delete()

        url_exitosa = reverse('autos')
        return redirect(url_exitosa)
    
def eliminar_camionetas(request, id): 
   
    camioneta = Camionetas.objects.get(id=id)
    
    if request.method == "POST":
        
        camioneta.delete()

        url_exitosa = reverse('camionetas')
        return redirect(url_exitosa)   

def eliminar_camiones(request, id): 
   
    camion = Camiones.objects.get(id=id)
    
    if request.method == "POST":
        
        camion.delete()

        url_exitosa = reverse('camiones')
        return redirect(url_exitosa)  

def eliminar_motos(request, id): 
   
    moto = motos.objects.get(id=id)
    
    if request.method == "POST":
        
        moto.delete()

        url_exitosa = reverse('motos')
        return redirect(url_exitosa) 

def eliminar_bicicletas(request, id): 
   
    bici = bicicletas.objects.get(id=id)
    
    if request.method == "POST":
        
        bici.delete()

        url_exitosa = reverse('bicicletas')
        return redirect(url_exitosa)                   
    
#Con estas view editamos

def editar_auto (request, id):
    Vehiculo = autos.objects.get(id=id)
    if request.method == "POST":
        formulario = Formulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            Vehiculo.marca = data ["marca"]
            Vehiculo.modelo = data ["modelo"]
            Vehiculo.ano = data ["ano"]
            Vehiculo.color = data ["color"]
            Vehiculo.equipamiento = data ["equipamiento"]
            Vehiculo.descripcion = data ["descripcion"]
            Vehiculo.save()
            url_exitosa = reverse('autos')
            return redirect(url_exitosa)
     
    else:
        inicial= {
            'marca' : Vehiculo.marca,
            'modelo' : Vehiculo.modelo,
            'ano' : Vehiculo.ano,
            'color' : Vehiculo.color,
            'equipamiento' : Vehiculo.equipamiento,
            'descripcion' : Vehiculo.descripcion
        }
        formulario = Formulario(initial=inicial)    
    Http_response = render(
        request = request,
        template_name = 'pre_entrega/formulario_crear_auto.html', 
        context={'formulario':formulario}
        )
    return Http_response

def editar_camionetas (request, id):
    Vehiculo = Camionetas.objects.get(id=id)
    if request.method == "POST":
        formulario = Formulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            Vehiculo.marca = data ["marca"]
            Vehiculo.modelo = data ["modelo"]
            Vehiculo.ano = data ["ano"]
            Vehiculo.color = data ["color"]
            Vehiculo.equipamiento = data ["equipamiento"]
            Vehiculo.descripcion = data ["descripcion"]
            Vehiculo.save()
            url_exitosa = reverse('camionetas')
            return redirect(url_exitosa)
     
    else:
        inicial= {
            'marca' : Vehiculo.marca,
            'modelo' : Vehiculo.modelo,
            'ano' : Vehiculo.ano,
            'color' : Vehiculo.color,
            'equipamiento' : Vehiculo.equipamiento,
            'descripcion' : Vehiculo.descripcion
        }
        formulario = Formulario(initial=inicial)    
    Http_response = render(
        request = request,
        template_name = 'pre_entrega/formulario_crear_camionetas.html', 
        context={'formulario':formulario}
        )
    return Http_response

def editar_camiones (request, id):
    Vehiculo = Camiones.objects.get(id=id)
    if request.method == "POST":
        formulario = Formulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            Vehiculo.marca = data ["marca"]
            Vehiculo.modelo = data ["modelo"]
            Vehiculo.ano = data ["ano"]
            Vehiculo.color = data ["color"]
            Vehiculo.equipamiento = data ["equipamiento"]
            Vehiculo.descripcion = data ["descripcion"]
            Vehiculo.save()
            url_exitosa = reverse('camiones')
            return redirect(url_exitosa)
     
    else:
        inicial= {
            'marca' : Vehiculo.marca,
            'modelo' : Vehiculo.modelo,
            'ano' : Vehiculo.ano,
            'color' : Vehiculo.color,
            'equipamiento' : Vehiculo.equipamiento,
            'descripcion' : Vehiculo.descripcion
        }
        formulario = Formulario(initial=inicial)    
    Http_response = render(
        request = request,
        template_name = 'pre_entrega/formulario_crear_camiones.html', 
        context={'formulario':formulario}
        )
    return Http_response

def editar_motos (request, id):
    Vehiculo = motos.objects.get(id=id)
    if request.method == "POST":
        formulario = Formulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            Vehiculo.marca = data ["marca"]
            Vehiculo.modelo = data ["modelo"]
            Vehiculo.ano = data ["ano"]
            Vehiculo.color = data ["color"]
            Vehiculo.equipamiento = data ["equipamiento"]
            Vehiculo.descripcion = data ["descripcion"]
            Vehiculo.save()
            url_exitosa = reverse('motos')
            return redirect(url_exitosa)
     
    else:
        inicial= {
            'marca' : Vehiculo.marca,
            'modelo' : Vehiculo.modelo,
            'ano' : Vehiculo.ano,
            'color' : Vehiculo.color,
            'equipamiento' : Vehiculo.equipamiento,
            'descripcion' : Vehiculo.descripcion
        }
        formulario = Formulario(initial=inicial)    
    Http_response = render(
        request = request,
        template_name = 'pre_entrega/formulario_crear_motos.html', 
        context={'formulario':formulario}
        )
    return Http_response

def editar_bicicletas (request, id):
    Vehiculo = bicicletas.objects.get(id=id)
    if request.method == "POST":
        formulario = Formulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            Vehiculo.marca = data ["marca"]
            Vehiculo.modelo = data ["modelo"]
            Vehiculo.ano = data ["ano"]
            Vehiculo.color = data ["color"]
            Vehiculo.equipamiento = data ["equipamiento"]
            Vehiculo.descripcion = data ["descripcion"]
            Vehiculo.save()
            url_exitosa = reverse('bicicletas')
            return redirect(url_exitosa)
     
    else:
        inicial= {
            'marca' : Vehiculo.marca,
            'modelo' : Vehiculo.modelo,
            'ano' : Vehiculo.ano,
            'color' : Vehiculo.color,
            'equipamiento' : Vehiculo.equipamiento,
            'descripcion' : Vehiculo.descripcion
        }
        formulario = Formulario(initial=inicial)    
    Http_response = render(
        request = request,
        template_name = 'pre_entrega/formulario_crear_bicicletas.html', 
        context={'formulario':formulario}
        )
    return Http_response