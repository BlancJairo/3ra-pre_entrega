from django.contrib import admin

from app_preentrega.models import autos, Camiones, Camionetas, motos, bicicletas

admin.site.register(autos)
admin.site.register(Camiones)
admin.site.register(Camionetas)
admin.site.register(motos)
admin.site.register(bicicletas)