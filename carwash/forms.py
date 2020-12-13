from django import forms
from .models import Marca, Cliente, Servicio, Automovil

class MarcaForm(forms.ModelForm):

    class Meta:
        model = Marca
        fields = ('nombre', 'Descripcion',)

class ServicioForm(forms.ModelForm):

    class Meta:
        model = Servicio
        fields = ('service', 'precio')


class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = ('nombres', 'apellidos', 'dpi', 'telefono', 'imagen')

class AutomovilForm(forms.ModelForm):

    class Meta:
        model = Automovil
        fields = ('placa', 'color', 'marca', 'cliente', 'servicio')
