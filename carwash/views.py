from django.shortcuts import render
from django.utils import timezone
from .models import Servicio

# POST SERVICIO
def lista_servicio(request):
    posts = Servicio.objects.filter().order_by('nombre')
    return render(request, 'blog/lista_servicio.html', {'posts': posts})
