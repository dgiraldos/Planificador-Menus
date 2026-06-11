from django.contrib import admin

# Register your models here.
from . models import Comida, Planificacion

admin.site.register(Comida)
admin.site.register(Planificacion)