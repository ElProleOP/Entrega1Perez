from django.contrib import admin

from AppEntrega.models import Libros, Socio, Juegomesa

# Register your models here.

admin.site.register(Libros)
admin.site.register(Socio)
admin.site.register(Juegomesa)