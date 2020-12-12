from django.db import models
from django.utils import timezone

class Servicio(models.Model):

    nombre = models.CharField(max_length=100)
    precio = models.CharField(max_length=100)

    def _str_(self):
        return self.nombre
        
class Cliente(models.Model):
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    dpi = models.CharField(max_length=10)
    telefono = models.CharField(max_length=20)
    imagen = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)

    def _str_(self):
        return self.nombres

class Marca(models.Model):
    nombre = models.CharField(max_length=50)
    Descripcion = models.TextField()

    def Marcapost(self):
        self.save()

    def eliminar(self):
        self.delete()

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name_plural="Marcas"

class Automovil(models.Model):
    placa = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    cliente_fk = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    servicio_fk = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    marca_fk = models.ForeignKey(Marca, on_delete=models.CASCADE)

    def _str_(self):
        return self.placa
    
    class Meta:
        verbose_name_plural="Automoviles"