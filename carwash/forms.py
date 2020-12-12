from django import forms

from .models import Marca, Cliente

class MarcaForm(forms.ModelForm):

    class Meta:
        model = Marca
        fields = ('nombre', 'Descripcion',)

class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = ('nombres', 'apellidos', 'dpi', 'telefono', 'imagen')