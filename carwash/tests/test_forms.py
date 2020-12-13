from django.test import SimpleTestCase
from carwash.forms import MarcaForm, ClienteForm

class MarcaTestForms(SimpleTestCase):

    def test_marca_form(self):
        form=MarcaForm(data={
            'nombre':'Prueba',
            'Descripcion':'Esto es una prueba'
        })
        self.assertTrue(form.is_valid())