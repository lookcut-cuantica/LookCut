from django.db import models
from datetime import date

class Barbero(models.Model):
    cedula = models.CharField(max_length=200)
    nombre = models.CharField(max_length=200)
    avatar = models.ImageField(upload_to="avatars")
    barberia = models.ForeignKey('Barberia', on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre

class Barberia(models.Model):
    nombre = models.CharField(max_length=200)
    latitud = models.CharField(max_length=200)
    longitud = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)  
    horario = models.CharField(max_length=200)
    def __str__(self):
        return self.nombre

class Servicio(models.Model):
    descripcion = models.TextField()
    nombre = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to="cortes")
    precio = models.CharField(max_length=200)
    barberia = models.ForeignKey('Barberia', on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre

class Turno(models.Model):
    barberia = models.ForeignKey('Barberia', on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.ForeignKey('Hora', on_delete=models.CASCADE)
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE)
    
class Hora(models.Model):
    hora = models.CharField(max_length=200)
    def __str__(self):
        return self.hora

class Cliente(models.Model):
    nombre = models.CharField(max_length=200)
    userName = models.CharField(max_length=200)
    contraseña = models.CharField(max_length=200)
    cedula = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre
           