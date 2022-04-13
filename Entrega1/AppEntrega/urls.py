from django.urls import path
from AppEntrega import views

urlpatterns = [

    path('', views.inicio ,  name='inicio'),
    path('libros/' , views.librosFormulario , name='Libros'),
    path('socios/' , views.sociosFormulario, name = 'Socios'),
    path('busquedaSocio/', views.busquedaSocio, name ='BusquedaSocio'),
    path('buscar/', views.buscar ),
    path('juegodemesa/', views.juegosFormulario , name= 'Juegomesa'),
]