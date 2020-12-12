from django.db import models
from django.utils import timezone

#SERVICIO 
class Servicio(models.Model):

    nombre = models.CharField(max_length=100)
    precio = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
