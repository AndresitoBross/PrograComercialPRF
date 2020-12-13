from django.test import TestCase
from carwash.models import Marca, Cliente, Servicio, Automovil


class MarcaTestModels(TestCase):

    @classmethod
    def setUpTestData(cls):
        Marca.objects.create(
            nombre='Prueba',
            Descripcion='Es una prueba'
        )
        pass

    def test_marca_nueva(self):
        marca = Marca.objects.get(id=1)
        field_label = marca._meta.get_field('nombre').verbose_name
        self.assertEquals(field_label, 'nombre')

    def test_marca_nombre_length(self):
        marca = Marca.objects.get(id=1)
        max_length = Marca._meta.get_field('nombre').max_length
        self.assertEquals(max_length, 50)


class ClienteTestModels(TestCase):

    @classmethod
    def setUpTestData(cls):
        Cliente.objects.create(
            nombres='Andres',
            apellidos='Es una prueba',
            dpi='1251651356',
            telefono='88888880',
            imagen='None/f.jpg'
        )
        pass

    def test_cliente_nuevo(self):
        cliente = Cliente.objects.get(id=1)
        field_label = cliente._meta.get_field('nombres').verbose_name
        self.assertEquals(field_label, 'nombres')

    def test_cliente_length(self):
        cliente = Cliente.objects.get(id=1)
        nombres_length = Cliente._meta.get_field('nombres').max_length
        apellidos_length = Cliente._meta.get_field('apellidos').max_length
        dpi_length = Cliente._meta.get_field('dpi').max_length
        telefono_length = Cliente._meta.get_field('telefono').max_length
        self.assertEquals(nombres_length, 50)
        self.assertEquals(apellidos_length, 50)
        self.assertEquals(dpi_length, 10)
        self.assertEquals(telefono_length, 8)


class ServicioTestModels(TestCase):

    @classmethod
    def setUpTestData(cls):
        Servicio.objects.create(
            service='Prueba',
            precio='10000'
        )
        pass

    def test_servicio_nueva(self):
        servicio = Servicio.objects.get(id=1)
        field_label = servicio._meta.get_field('service').verbose_name
        self.assertEquals(field_label, 'service')

    def test_servicio_length(self):
        servicio = Servicio.objects.get(id=1)
        service_length = Servicio._meta.get_field('service').max_length
        precio_length = Servicio._meta.get_field('precio').max_length
        self.assertEquals(service_length, 50)
        self.assertEquals(precio_length, 50)


class AutomovilTestModels(TestCase):

    @classmethod
    def setUpTestData(cls):
        marcas = Marca.objects.create(
            nombre='Prueba',
            Descripcion='Es una prueba'
        )
        clientes = Cliente.objects.create(
            nombres='Andres',
            apellidos='Es una prueba',
            dpi='1251651356',
            telefono='88888880',
            imagen='None/f.jpg'
        )
        servicios = Servicio.objects.create(
            service='Prueba',
            precio='10000'
        )
        Automovil.objects.create(
            placa='WASD9-W',
            color='azul',
            cliente=clientes,
            servicio=servicios,
            marca=marcas
        )
        pass

    def test_automovil_nueva(self):
        automovil = Automovil.objects.get(id=1)
        field_label = Automovil._meta.get_field('placa').verbose_name
        self.assertEquals(field_label, 'placa')

    def test_automovil_length(self):
        automovil = Automovil.objects.get(id=1)
        placa_length = Automovil._meta.get_field('placa').max_length
        color_length = Automovil._meta.get_field('color').max_length
        self.assertEquals(placa_length, 50)
        self.assertEquals(color_length, 50)
