from django import forms
from .models import Marca, Servicio

class MarcaForm(forms.ModelForm):

    class Meta:
        model = Marca
        fields = ('nombre', 'Descripcion',)


class ServicioForm(forms.ModelForm):
    class Meta:
        model: Servicio
        fields = ('nombre', 'precio',)