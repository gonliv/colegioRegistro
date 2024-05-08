from django.contrib import admin

# Register your models here.

from .models import Estudiante, Profesor, Curso, Direccion

admin.site.register(Estudiante)
admin.site.register(Profesor)
admin.site.register(Curso)
admin.site.register(Direccion)