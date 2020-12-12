from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_servicio, name='lista_servicio'),
]