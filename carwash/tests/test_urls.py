from django.test import TestCase, SimpleTestCase
from django.urls import reverse,resolve
from carwash.views import marca_lista, marca_eliminar, marca_nueva, marca_editar, cliente_lista,cliente_nuevo,cliente_eliminar,cliente_eliminar, lista_servicio

class MarcaUrls(SimpleTestCase):
    
    def test_url_lista_resolved(self):
        url = reverse('marca_lista')
        self.assertEquals(resolve(url).func,marca_lista)
    
    def test_url_nueva_resolved(self):
        url = reverse('marca_nueva')
        self.assertEquals(resolve(url).func,marca_nueva)
    
    #def test_url_eliminar_resolved(self):
    #    url = reverse('marca_eliminar',args=['some-marca'])
    #    print(resolve(url))
        #self.assertEquals(resolve(url).func,marca_eliminar)
class ClienteUrls(SimpleTestCase):
    
    def test_url_lista_resolved(self):
        url = reverse('cliente_lista')
        self.assertEquals(resolve(url).func,cliente_lista)
    
    def test_url_nueva_resolved(self):
        url = reverse('cliente_nuevo')
        self.assertEquals(resolve(url).func,cliente_nuevo)

class ListaUrls(SimpleTestCase):
    
    def test_url_lista_resolved(self):
        url = reverse('lista_servicio')
        self.assertEquals(resolve(url).func,lista_servicio)
