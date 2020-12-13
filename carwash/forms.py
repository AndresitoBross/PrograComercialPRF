from django import forms
from .models import Marca, Cliente, Servicio

class MarcaForm(forms.ModelForm):

    class Meta:
        model = Marca
        fields = ('nombre', 'Descripcion',)


class ServicioForm(forms.ModelForm):

    class Meta:
        model: Servicio
        fields = ('nombre', 'precio')

class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = ('nombres', 'apellidos', 'dpi', 'telefono', 'imagen')
