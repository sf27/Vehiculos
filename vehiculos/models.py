# -*- coding: utf-8 -*-
from django.db import models

class Marca(models.Model):
    marca = models.CharField(max_length=150, null=False, unique=True)
    fecha_registro = models.DateTimeField(auto_now=True)
    def __unicode__(self):
        return '-'.join([self.marca])

class Institucion(models.Model):
    institucion = models.CharField(max_length=150, null=False, unique=True)
    fecha_registro = models.DateTimeField(auto_now=True)
    def __unicode__(self):
        return '-'.join([self.institucion])

class Vehiculo(models.Model):
    placas = models.CharField(max_length=150, null=False)
    modelo = models.CharField(max_length=150, null=False)
    anyo = models.PositiveIntegerField()
    marca = models.ForeignKey(Marca)
    institucion = models.ForeignKey(Institucion)
    fecha_vencimiento = models.DateField()
    foto = models.ImageField(upload_to='vehiculos')
    fecha_registro = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '-'.join([self.placas, self.modelo])

