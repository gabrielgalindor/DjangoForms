from django.urls import path
from django.urls import path 
from .views import Home, registrarPredio

urlpatterns= [
    path('',Home, name='index'),
    path('registrar_predio/', registrarPredio, name= 'registrar_predio')
]