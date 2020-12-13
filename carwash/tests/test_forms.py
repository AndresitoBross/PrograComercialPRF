from django.test import SimpleTestCase, TestCase
from carwash.forms import MarcaForm, ClienteForm, ServicioForm, AutomovilForm
from carwash.models import Marca,Cliente,Servicio,Automovil
class MarcaTestForms(SimpleTestCase):

    def test_marca_form(self):
        form=MarcaForm(data={
            'nombre':'Prueba',
            'Descripcion':'Esto es una prueba'
        })
        self.assertTrue(form.is_valid())

class ClienteTestForms(TestCase):
    
    def test_cliente_form(self):
        form=ClienteForm(data={
            'nombres':'Prueba de prueba',
            'apellidos':'test',
            'dpi':'777889897',
            'telefono':'80896459',
            'imagen':'None/a.jpg'
        })
        self.assertTrue(form.is_valid())

class ServicioTestForms(SimpleTestCase):

    def test_servicio_form(self):
        form=ServicioForm(data={
            'service':'servicio de prueba',
            'precio':'1000'
        })
        self.assertTrue(form.is_valid())

class AutomovilTestForms(TestCase):
    @classmethod
    def setUpTestData(cls):
        Marca.objects.create(
            nombre='Prueba',
            Descripcion='Es una prueba'
        )
        Cliente.objects.create(
            nombres='Andres',
            apellidos='Es una prueba',
            dpi = '1251651356',
            telefono='88888880',
            imagen='None/f.jpg'
        )
        Servicio.objects.create(
            service='Prueba',
            precio='10000'
        )
        pass

    def test_automovil_form(self):
        marca=Marca.objects.get(id=1).pk
        cliente=Cliente.objects.get(id=1).pk
        servicio=Servicio.objects.get(id=1).pk
        form=AutomovilForm(data={
            'placa':'X090-P',
            'color':'Esto es una prueba',
            'marca': marca,
            'cliente':cliente,
            'servicio':servicio
       })
        self.assertTrue(form.is_valid())