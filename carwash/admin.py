from django.contrib import admin
<<<<<<< HEAD
from .models import Servicio

#SERVICIO
admin.site.register(Servicio)
=======
from .models import Marca, Cliente, Servicio

admin.site.register(Marca)
admin.site.register(Cliente)
admin.site.register(Servicio)
>>>>>>> master
