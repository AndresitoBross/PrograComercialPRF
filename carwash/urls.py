from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
    path('', views.lista_servicio, name='lista_servicio'),
    path('', views.marca_lista, name='marca_lista'),
    path('marca/nueva', views.marca_nueva, name='marca_nueva'),
    path('marca/<int:pk>/editar/', views.marca_editar, name='marca_editar'),
    path('marca/<int:pk>/eliminar/', views.marca_eliminar, name='marca_eliminar'),
]