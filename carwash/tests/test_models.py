from django.test import TestCase
from carwash.models import Marca,Cliente,Servicio

class MarcaTestModels(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        Marca.objects.create(
            nombre='Prueba',
            Descripcion='Es una prueba'
        )
        pass

    def test_marca_nueva (self):
        marca=Marca.objects.get(id=1)
        field_label = marca._meta.get_field('nombre').verbose_name
        self.assertEquals(field_label,'nombre')
    
    def test_marca_nombre_length (self):
        marca=Marca.objects.get(id=1)
        max_length = Marca._meta.get_field('nombre').max_length
        self.assertEquals(max_length,50)

class ClienteTestModels(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        Cliente.objects.create(
            nombres='Andres',
            apellidos='Es una prueba',
            dpi = '1251651356',
            telefono='88888880',
            imagen='None/f.jpg'
        )
        pass

    def test_cliente_nuevo (self):
        cliente=Cliente.objects.get(id=1)
        field_label = cliente._meta.get_field('nombres').verbose_name
        self.assertEquals(field_label,'nombres')
    
    def test_cliente_length (self):
        cliente=Cliente.objects.get(id=1)
        nombres_length = Cliente._meta.get_field('nombres').max_length
        apellidos_length = Cliente._meta.get_field('apellidos').max_length
        dpi_length = Cliente._meta.get_field('dpi').max_length
        telefono_length = Cliente._meta.get_field('telefono').max_length
        self.assertEquals(nombres_length,50)
        self.assertEquals(apellidos_length,50)
        self.assertEquals(dpi_length,10)
        self.assertEquals(telefono_length,8)    