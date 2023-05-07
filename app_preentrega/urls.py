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

from app_preentrega.views import lista_autos, lista_camionetas, lista_camiones, lista_motos, lista_bicicletas

urlpatterns = [
    path('lista_autos/', lista_autos),
    path('lista_camionetas/', lista_camionetas),
    path('lista_camiones/', lista_camiones),
    path('lista_motos/', lista_motos),
    path('lista_bicicletas/', lista_bicicletas),
]
