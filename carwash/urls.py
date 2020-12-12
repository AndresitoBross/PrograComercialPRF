from django.urls import path
from . import views

urlpatterns = [
    #Servicio
    path('servicio', views.lista_servicio, name='lista_servicio'),
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
]