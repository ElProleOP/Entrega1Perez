from django.db import models

# Create your models here.

class Libros(models.Model):

    genero = models.CharField(max_length=40)
    titulo = models.CharField(max_length=60)
    numero_de_guia = models.IntegerField()

class Socio(models.Model):

    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    edad = models.IntegerField()
    email = models.EmailField()

class Juegomesa(models.Model):

    titulo = models.CharField(max_length=40)
    numero_de_guia = models.IntegerField()
    precio = models.IntegerField()


