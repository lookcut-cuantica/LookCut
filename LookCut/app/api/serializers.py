from rest_framework import serializers
from .models import (
    Cliente,
    Hora,
    Turno,
    Servicio,
    Barberia,
    Barbero
)


class ServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicio
        fields = ('id', 'nombre', 'imagen', 'precio', 'barberia')

class BarberoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Barbero
        fields = ('id', 'nombre', 'avatar', 'barberia')


class BarberiaSerializer(serializers.ModelSerializer):
    barberos = BarberoSerializer(read_only=True, many=True)
    servicios = ServicioSerializer(read_only=True, many=True)
    class Meta:
        model = Barberia
        fields = ('nombre', 'latitud', 'longitud', 'direccion', 'horario','servicios','barberos')

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ('id', 'nombre', 'userName', 'barberia')
