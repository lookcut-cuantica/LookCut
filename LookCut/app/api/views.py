from django.shortcuts import render
from rest_framework.parsers import JSONParser
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg import openapi

from .models import (
    Cliente,
    Hora,
    Turno,
    Servicio,
    Barberia,
    Barbero
)


from .serializers import BarberiaSerializer, ServicioSerializer, BarberoSerializer



class barberos(APIView):
    parser_classes = (JSONParser,)
    @swagger_auto_schema(
        responses={200:openapi.Response('Barbero',BarberoSerializer)}
    )
    def get(self, request):
        obj = Barbero.objects.all()
        serializer = BarberoSerializer(obj, many=True)
        return Response(serializer.data)

class barberias(APIView):
    parser_classes = (JSONParser,)
    @swagger_auto_schema(
        responses={200:openapi.Response('Barberia',BarberiaSerializer)}
    )
    def get(self, request):
        obj = Barberia.objects.all()
        serializer = BarberiaSerializer(instance = obj, many=True)
        return Response(serializer.data)


class servicios(APIView):
    parser_classes = (JSONParser,)
    @swagger_auto_schema(
        responses={200:openapi.Response('Servicios',ServicioSerializer)}
    )
    def get(self, request):
        obj = Servicio.objects.all()
        serializer = ServicioSerializer(instance = obj, many=True)
        return Response(serializer.data)