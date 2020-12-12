from django.urls import path
from . import views

urlpatterns = [
    path('servicio', views.lista_servicio, name='lista_servicio'),
    path('servicio/nueva', views.servicio_nueva, name='servicio_nueva'),
    path('servicio/<int:pk>/editar/', views.servicio_editar, name='servicio_editar'),
    path('servicio/<int:pk>/eliminar/', views.servicio_eliminar, name='servicio_eliminar'),
    path('marca', views.marca_lista, name='marca_lista'),
    path('marca/nueva', views.marca_nueva, name='marca_nueva'),
    path('marca/<int:pk>/editar/', views.marca_editar, name='marca_editar'),
    path('marca/<int:pk>/eliminar/', views.marca_eliminar, name='marca_eliminar'),
]