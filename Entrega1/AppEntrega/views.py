from django.shortcuts import render , HttpResponse
from django.http import HttpResponse
from AppEntrega.forms import LibroFormulario, SocioFormulario, JuegoFormulario
from AppEntrega.models import Libros, Socio , Juegomesa

# Create your views here.

def inicio(request):

      return render(request, "AppEntrega/inicio.html")

def librosFormulario(request):

      if request.method == 'POST':
            
            miformulario = LibroFormulario(request.POST)

            print(miformulario)
            
            if miformulario.is_valid:

                  informacion = miformulario.cleaned_data

                  libro = Libros(genero=informacion['genero'], titulo = informacion['titulo'], 
                  numero_de_guia = informacion ['numero_de_guia'])

                  libro.save()

                  return render(request, "AppEntrega/inicio.html")
      else:

            miformulario = LibroFormulario()

      return render(request, "AppEntrega/librosFormulario.html", {"miFormulario":miformulario})

def sociosFormulario(request):

      if request.method == 'POST':
            
            miformulario2 = SocioFormulario(request.POST)

            print(miformulario2)
            
            if miformulario2.is_valid:

                  informacion2 = miformulario2.cleaned_data

                  socio = Socio(nombre=informacion2['nombre'], apellido = informacion2['apellido'],
                   edad = informacion2 ['edad'], email = informacion2 ['email'])

                  socio.save()

                  return render(request, "AppEntrega/inicio.html")
      else:

            miformulario2 = SocioFormulario()

      return render(request, "AppEntrega/sociosFormulario.html", {"miFormulario2":miformulario2})

def busquedaSocio(request):

      return render(request, 'AppEntrega/busquedaSocio.html')

def buscar(request):

      if request.method == "GET":

           email = request.GET['email']
           print(email)
           socios = Socio.objects.filter(email__icontains = email)
           print(socios)
           return render(request, 'AppEntrega/resultadoBusqueda.html', {'socios':socios , 'email':email})

      else:
            respuesta = "No enviaste nada"
      return HttpResponse (respuesta)

def juegosFormulario(request):

      if request.method == 'POST':
            
            miformulario3 = JuegoFormulario(request.POST)

            print(miformulario3)
            
            if miformulario3.is_valid:

                  informacion3 = miformulario3.cleaned_data

                  juego = Juegomesa(titulo=informacion3['titulo'],
                   numero_de_guia = informacion3 ['numero_de_guia'], precio = informacion3 ['precio'])

                  juego.save()

                  return render(request, "AppEntrega/inicio.html")
      else:

            miformulario3 = JuegoFormulario()

      return render(request, "AppEntrega/juegosFormulario.html", {"miFormulario3":miformulario3})

