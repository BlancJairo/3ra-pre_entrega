"""
URL configuration for pre_entrega project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path

from app_preentrega.views import lista_autos, lista_camionetas, lista_camiones, lista_motos, lista_bicicletas,\
    subir_autos, subir_camionetas, subir_camiones, subir_motos,subir_bicicletas,\
    buscar_auto, buscar_camionetas, buscar_camiones, buscar_camiones, buscar_bicicletas, buscar_motos,\
    eliminar_auto, eliminar_camionetas, eliminar_camiones, eliminar_motos, eliminar_bicicletas,\
    editar_auto, editar_camionetas, editar_camiones, editar_motos, editar_bicicletas

urlpatterns = [
    # Path de listar
    path('lista_autos/', lista_autos, name="autos"),
    path('lista_camionetas/', lista_camionetas, name="camionetas"),
    path('lista_camiones/', lista_camiones, name="camiones"),
    path('lista_motos/', lista_motos, name="motos"),
    path('lista_bicicletas/', lista_bicicletas, name="bicicletas"),
    # Path de subir
    path('subir-autos/', subir_autos, name="subir_autos"),
    path('subir-camionetas/', subir_camionetas, name="subir_camionetas"),
    path('subir-camiones/', subir_camiones, name="subir_camiones"),
    path('subir-motos/', subir_motos, name="subir_motos"),
    path('subir-bicicletas/', subir_bicicletas, name="subir_bicicletas"),
    # Path de buscar
    path('buscar-autos/', buscar_auto, name="buscar_auto"),
    path('buscar-camionetas/', buscar_camionetas, name="buscar_camionetas"),
    path('buscar-camiones/', buscar_camiones, name="buscar_camiones"),
    path('buscar-bicicletas/', buscar_bicicletas, name="buscar_bicicletas"),
    path('buscar-motos/', buscar_motos, name="buscar_motos"),
    # Path de eliminar
    path('eliminar-autos/<int:id>/', eliminar_auto, name="eliminar_auto"),
    path('eliminar-camionetas/<int:id>/', eliminar_camionetas, name="eliminar_camionetas"),
    path('eliminar-camiones/<int:id>/', eliminar_camiones, name="eliminar_camiones"),
    path('eliminar-motos/<int:id>/', eliminar_motos, name="eliminar_motos"),
    path('eliminar-bicicletas/<int:id>/', eliminar_bicicletas, name="eliminar_bicicletas"),   
    # Path de editar
    path('editar-autos/<int:id>/', editar_auto, name="editar_auto"),
    path('editar-camionetas/<int:id>/', editar_camionetas, name="editar_camionetas"),
    path('editar-camiones/<int:id>/', editar_camiones, name="editar_camiones"),
    path('editar-motos/<int:id>/', editar_motos, name="editar_motos"),
    path('editar-bicicletas/<int:id>/', editar_bicicletas, name="editar_bicicletas"),
]
