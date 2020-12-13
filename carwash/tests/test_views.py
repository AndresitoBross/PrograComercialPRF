from django.test import TestCase, Client
from django.urls import reverse
from carwash.models import Marca, Cliente, Servicio
import json


class MarcaTestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.lista_url = reverse('marca_lista')
        self.nueva_url = reverse('marca_nueva')
        self.eliminar_url = reverse('marca_eliminar', kwargs={'pk': 1})
        self.editar_url = reverse('marca_editar',kwargs={'pk': 1})

    def test_marca_lista_GET(self):
        response = self.client.get(self.lista_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/marca_lista.html')

    def test_marca_nueva_POST(self):
        response = self.client.get(self.nueva_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/marca_editar.html')

class ClienteTestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.lista_url = reverse('cliente_lista')
        self.nueva_url = reverse('cliente_nuevo')

    def test_cliente_lista_GET(self):
        response = self.client.get(self.lista_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/cliente_lista.html')

    def test_cliente_nueva_GET(self):
        response = self.client.get(self.nueva_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/cliente_editar.html')


class ServicioTestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.lista_url = reverse('lista_servicio')
        self.nueva_url = reverse('servicio_nuevo')

    def test_servicio_lista_GET(self):
        response = self.client.get(self.lista_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/lista_servicio.html')

    def test_servicio_nueva_GET(self):
        response = self.client.get(self.nueva_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/servicio_editar.html')


class AutomovilTestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.lista_url = reverse('automovil_lista')
        self.nueva_url = reverse('automovil_nuevo')

    def test_automovil_lista_GET(self):
        response = self.client.get(self.lista_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/automovil_lista.html')

    def test_automovil_nueva_GET(self):
        response = self.client.get(self.nueva_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/automovil_editar.html')
