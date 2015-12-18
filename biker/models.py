from __future__ import unicode_literals

from django.db import models

class Grupo(models.Model):
	nombre_grupo = models.CharField(max_length = 30)
	def __str__(self):
		return self.nombre_grupo

class Usuario(models.Model):
	nombre = models.CharField(max_length = 30)
	correo = models.EmailField(max_length = 50)
	fecha_nacimiento = models.DateTimeField()
	grupos = models.ManyToManyField(Grupo, related_name = 'usuarios', default = None)
	def __str__(self):
		return self.nombre

class Ruta(models.Model):
	nombre_ruta = models.CharField(max_length = 30)
	distancia = models.FloatField()
	usuario = models.ForeignKey(Usuario)
	def __str__(self):
		return self.nombre_ruta

class  Evento(models.Model):
	nombre_evento = models.CharField(max_length = 30)
	punto_partida = models.CharField(max_length = 30)
	fecha_partida = models.DateTimeField(blank=True, null=True)
	ruta = models.ForeignKey(Ruta)
	grupo = models.ForeignKey(Grupo)
	def __str__(self):
		return self.nombre_evento
# Create your models here.
