from django.urls import path, include
from . import views

urlpatterns = [
    #Home
    path('', views.home, name='home'),
    #Servicio
    path('servicio', views.lista_servicio, name='lista_servicio'),
    path('servicio/nuevo', views.servicio_nuevo, name='servicio_nuevo'),
    path('servicio/<int:pk>/editar/', views.servicio_editar, name='servicio_editar'),
    path('servicio/<int:pk>/eliminar/', views.servicio_eliminar, name='servicio_eliminar'),
    #Marca
    path('marca', views.marca_lista, name='marca_lista'),
    path('marca/nueva', views.marca_nueva, name='marca_nueva'),
    path('marca/<int:pk>/editar/', views.marca_editar, name='marca_editar'),
    path('marca/<int:pk>/eliminar/', views.marca_eliminar, name='marca_eliminar'),
    #Cliente
    path('cliente', views.cliente_lista, name='cliente_lista'),
    path('cliente/nuevo', views.cliente_nuevo, name='cliente_nuevo'),
    path('cliente/<int:pk>/editar/', views.cliente_editar, name='cliente_editar'),
    path('cliente/<int:pk>/eliminar/', views.cliente_eliminar, name='cliente_eliminar'),
    #Automovil
    path('automovil', views.automovil_lista, name='automovil_lista'),
    path('automovil/nuevo', views.automovil_nuevo, name='automovil_nuevo'),
    path('automovil/<int:pk>/editar/', views.automovil_editar, name='automovil_editar'),
    path('automovil/<int:pk>/eliminar/', views.automovil_eliminar, name='automovil_eliminar'),
]