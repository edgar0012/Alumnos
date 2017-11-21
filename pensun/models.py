from django.db import models

from django.contrib import admin


class Alumno(models.Model):
    nombre  =   models.CharField(max_length=30)
    anio    = models.IntegerField()
    sexo    = models.CharField(max_length=60)

    def __str__(self):
        return self.nombre

class Profesor(models.Model):
    nombre  =   models.CharField(max_length=30)
    especialiadad    = models.CharField(max_length=60)
    sexo    = models.CharField(max_length=60)
    

    def __str__(self):
        return self.nombre

class Materia(models.Model):
    nombre  =   models.CharField(max_length=30)
    seccion    = models.CharField(max_length=60)
    aula    = models.CharField(max_length=60)

    def __str__(self):
        return self.nombre

class Pensun(models.Model):
    nombre    = models.CharField(max_length=60)
    materias   = models.ManyToManyField(Materia, through='Asignacion')

    def __str__(self):
        return self.nombre

class Asignacion (models.Model):

    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    pensun = models.ForeignKey(Pensun, on_delete=models.CASCADE)


class AsignacionInLine(admin.TabularInline):
    model = Asignacion
    extra = 1


class MateriaAdmin(admin.ModelAdmin):
    inlines = (AsignacionInLine,)


class PensunAdmin (admin.ModelAdmin):
    inlines = (AsignacionInLine,)
