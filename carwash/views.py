from django.shortcuts import render, get_object_or_404, redirect
#from django.contrib.auth.decorators import login_required
from .models import Marca, Servicio, Cliente, Automovil
from .forms import MarcaForm, ClienteForm, ServicioForm, AutomovilForm

#Servicio
def lista_servicio(request):
    posts = Servicio.objects.filter().order_by('service')
    return render(request, 'blog/lista_servicio.html', {'posts': posts})

def servicio_nuevo(request):
    if request.method == "POST":
        formulario = ServicioForm(request.POST)
        if formulario.is_valid():
            servicio = formulario.save(commit=False)
            servicio.save()
            return redirect('lista_servicio')
    else:
        formulario = ServicioForm()
    return render(request, 'blog/servicio_editar.html', {'formulario': formulario})

def servicio_editar(request, pk):
    servicio = get_object_or_404(Servicio, pk=pk)
    if request.method == "POST":
        formulario = ServicioForm(request.POST, instance=servicio)
        if formulario.is_valid():
            servicio = formulario.save(commit=False)
            servicio.save()
            return redirect('lista_servicio')
    else: 
        formulario = ServicioForm(instance=servicio)
    return render(request, 'blog/servicio_editar.html', {'formulario': formulario})

def servicio_eliminar(request, pk):
    servicio = get_object_or_404(Servicio, pk=pk)
    servicio.eliminar()
    return redirect('lista_servicio')

#Marca
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

#Cliente
def cliente_lista(request):
    client = Cliente.objects.filter().order_by('nombres')
    return render(request, 'blog/cliente_lista.html', {'client':client})

def cliente_nuevo(request):
    if request.method == "POST":
        formulario = ClienteForm(request.POST)
        if formulario.is_valid():
            cliente = formulario.save(commit=False)
            cliente.save()
            return redirect('cliente_lista')
    else:
        formulario = ClienteForm()
    return render(request, 'blog/cliente_editar.html', {'formulario': formulario})

def cliente_editar(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == "POST":
        formulario = ClienteForm(request.POST, instance=cliente)
        if formulario.is_valid():
            cliente = formulario.save(commit=False)
            cliente.save()
            return redirect('cliente_lista')
    else:
        formulario = ClienteForm(instance=cliente)
    return render(request, 'blog/cliente_editar.html', {'formulario': formulario})

def cliente_eliminar(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    cliente.eliminar()
    return redirect('cliente_lista')

#Automovil
def automovil_lista(request):
    automoviles = Automovil.objects.filter().order_by('placa')
    return render(request, 'blog/automovil_lista.html', {'automoviles':automoviles})

def automovil_nuevo(request):
    if request.method == "POST":
        formulario = AutomovilForm(request.POST)
        if formulario.is_valid():
            automovil = formulario.save(commit=False)
            automovil.save()
            return redirect('automovil_lista')
    else:
        formulario = AutomovilForm()
    return render(request, 'blog/automovil_editar.html', {'formulario': formulario})

def automovil_editar(request, pk):
    automovil = get_object_or_404(Automovil, pk=pk)
    if request.method == "POST":
        formulario = AutomovilForm(request.POST, instance=automovil)
        if formulario.is_valid():
            automovil = formulario.save(commit=False)
            automovil.save()
            return redirect('automovil_lista')
    else:
        formulario = AutomovilForm(instance=automovil)
    return render(request, 'blog/automovil_editar.html', {'formulario': formulario})

def automovil_eliminar(request, pk):
    automovil = get_object_or_404(Automovil, pk=pk)
    automovil.eliminar()
    return redirect('automovil_lista')