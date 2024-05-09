from .models import Estudiante, Profesor, Curso, Direccion
from django.utils import timezone

# Funciones para crear entidades
def crear_curso(codigo, nombre, version=None, profesor_id=None):
    profesor = Profesor.objects.get(rut=profesor_id) if profesor_id else None
    curso = Curso.objects.create(codigo=codigo, nombre=nombre, version=version, profesor=profesor)
    return curso

def crear_profesor(rut, nombre, apellido, creado_por):
    return Profesor.objects.create(
        rut=rut,
        nombre=nombre,
        apellido=apellido,
        activo=False,
        creacion_registro=timezone.now(),
        modificacion_registro=timezone.now(),
        creado_por=creado_por
    )

def crear_estudiante(rut, nombre, apellido, fecha_nacimiento, creado_por):
    return Estudiante.objects.create(
        rut=rut,
        nombre=nombre,
        apellido=apellido,
        fecha_nacimiento=fecha_nacimiento,
        activo=False,
        creacion_registro=timezone.now(),
        modificacion_registro=timezone.now(),
        creado_por=creado_por
    )

def crear_direccion(estudiante_id, calle, numero, departamento, comuna, ciudad, region):
    estudiante = Estudiante.objects.get(rut=estudiante_id)
    return Direccion.objects.create(
        estudiante=estudiante,
        calle=calle,
        numero=numero,
        departamento=departamento,
        comuna=comuna,
        ciudad=ciudad,
        region=region
    )

# Funciones para obtener datos
def obtiene_estudiante(rut):
    return Estudiante.objects.get(rut=rut)

def obtiene_profesor(rut):
    return Profesor.objects.get(rut=rut)

def obtiene_curso(codigo):
    return Curso.objects.get(codigo=codigo)

# Funciones para manipular relaciones
def agrega_profesor_a_curso(profesor_id, codigo_curso):
    profesor = Profesor.objects.get(rut=profesor_id)
    curso = Curso.objects.get(codigo=codigo_curso)
    curso.profesor = profesor
    curso.save()

def agrega_cursos_a_estudiante(estudiante_id, lista_codigos_cursos):
    estudiante = Estudiante.objects.get(rut=estudiante_id)
    for codigo in lista_codigos_cursos:
        curso = Curso.objects.get(codigo=codigo)
        estudiante.cursos.add(curso)


def imprime_estudiante_cursos(rut):
    estudiante = Estudiante.objects.get(rut=rut)
    cursos = estudiante.cursos.all()
    return [curso.nombre for curso in cursos]
