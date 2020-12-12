from django.shortcuts import render, get_object_or_404, redirect
#from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Marca
from .forms import MarcaForm

def marca_lista(request):
    marces = Marca.objects.filter().order_by('nombre')
    return render(request, 'blog/marca_lista.html', {'marces':marces})

def marca_nueva(request):
    if request.method == "POST":
        formulario = MarcaForm(request.POST)
        if formulario.is_valid():
            marca = formulario.save(commit=False)
            marca.save()
            return redirect('marca_lista')
    else:
        formulario = MarcaForm()
    return render(request, 'blog/marca_editar.html', {'formulario': formulario})

def marca_editar(request, pk):
    marca = get_object_or_404(Marca, pk=pk)
    if request.method == "POST":
        formulario = MarcaForm(request.POST, instance=marca)
        if formulario.is_valid():
            marca = formulario.save(commit=False)
            marca.save()
            return redirect('marca_lista')
    else:
        formulario = MarcaForm(instance=marca)
    return render(request, 'blog/marca_editar.html', {'formulario': formulario})


def marca_eliminar(request, pk):
    marca = get_object_or_404(Marca, pk=pk)
    marca.eliminar()
    return redirect('marca_lista')
