from django.db import models

# Create your models here.

from django.db import models

class Estudiante(models.Model):
    rut = models.CharField(max_length=9, primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    activo = models.BooleanField(default=False)
    creacion_registro = models.DateField()
    modificacion_registro = models.DateField()
    creado_por = models.CharField(max_length=50)

class Direccion(models.Model):
    estudiante = models.OneToOneField(Estudiante, on_delete=models.CASCADE, primary_key=True)
    calle = models.CharField(max_length=50)
    numero = models.CharField(max_length=10)
    departamento = models.CharField(max_length=10)
    comuna = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)
    region = models.CharField(max_length=50)

class Profesor(models.Model):
    rut = models.CharField(max_length=9, primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    activo = models.BooleanField(default=False)
    creacion_registro = models.DateField()
    modificacion_registro = models.DateField()
    creado_por = models.CharField(max_length=50)

class Curso(models.Model):
    codigo = models.CharField(max_length=10, unique=True, primary_key=True)
    nombre = models.CharField(max_length=50)
    version = models.IntegerField(null=True, blank=True)
    profesor = models.OneToOneField(Profesor, on_delete=models.SET_NULL, null=True, blank=True)