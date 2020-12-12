from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_Servicio, name='post_Servicio'),
]