from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from carwash.views import marca_lista, marca_eliminar, marca_nueva, marca_editar, cliente_lista, cliente_nuevo, cliente_editar, cliente_eliminar, lista_servicio, servicio_nuevo, servicio_editar, servicio_eliminar, automovil_editar, automovil_eliminar, automovil_lista, automovil_nuevo, registerPage


class MarcaUrls(SimpleTestCase):

    def test_url_lista_resolved(self):
        url = reverse('marca_lista')
        self.assertEquals(resolve(url).func, marca_lista)

    def test_url_nueva_resolved(self):
        url = reverse('marca_nueva')
        self.assertEquals(resolve(url).func, marca_nueva)

    def test_url_eliminar_resolved(self):
        url = reverse('marca_eliminar', kwargs={'pk': 1})
        self.assertEquals(resolve(url).func, marca_eliminar)

    def test_url_editar_resolved(self):
        url = reverse('marca_editar', kwargs={'pk': 1})
        self.assertEquals(resolve(url).func, marca_editar)


class ClienteUrls(SimpleTestCase):

    def test_url_lista_resolved(self):
        url = reverse('cliente_lista')
        self.assertEquals(resolve(url).func, cliente_lista)

    def test_url_nueva_resolved(self):
        url = reverse('cliente_nuevo')
        self.assertEquals(resolve(url).func, cliente_nuevo)

    def test_url_eliminar_resolved(self):
        url = reverse('cliente_eliminar', kwargs={'pk': 1})
        self.assertEquals(resolve(url).func, cliente_eliminar)

    def test_url_editar_resolved(self):
        url = reverse('cliente_editar', kwargs={'pk': 1})
        self.assertEquals(resolve(url).func, cliente_editar)


class ServicioUrls(SimpleTestCase):

    def test_url_lista_resolved(self):
        url = reverse('lista_servicio')
        self.assertEquals(resolve(url).func, lista_servicio)

    def test_url_nueva_resolved(self):
        url = reverse('servicio_nuevo')
        self.assertEquals(resolve(url).func, servicio_nuevo)

    def test_url_eliminar_resolved(self):
        url = reverse('servicio_eliminar', kwargs={'pk': 1})
        self.assertEquals(resolve(url).func, servicio_eliminar)

    def test_url_editar_resolved(self):
        url = reverse('servicio_editar', kwargs={'pk': 1})
        self.assertEquals(resolve(url).func, servicio_editar)


class AutomovilUrls(SimpleTestCase):

    def test_url_lista_resolved(self):
        url = reverse('automovil_lista')
        self.assertEquals(resolve(url).func, automovil_lista)

    def test_url_nueva_resolved(self):
        url = reverse('automovil_nuevo')
        self.assertEquals(resolve(url).func, automovil_nuevo)

    def test_url_eliminar_resolved(self):
        url = reverse('automovil_eliminar', kwargs={'pk': 1})
        self.assertEquals(resolve(url).func, automovil_eliminar)

    def test_url_editar_resolved(self):
        url = reverse('automovil_editar', kwargs={'pk': 1})
        self.assertEquals(resolve(url).func, automovil_editar)

class RegistroUrls(SimpleTestCase):

    def test_url_lista_resolved(self):
        url = reverse('registerPage')
        self.assertEquals(resolve(url).func, registerPage)