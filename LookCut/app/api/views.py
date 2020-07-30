from django.shortcuts import render
from rest_framework.parsers import JSONParser
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg import openapi
from rest_framework import status

from .models import (
    Cliente,
    Hora,
    Turno,
    Servicio,
    Barberia,
    Barbero
)


from .serializers import (
    BarberiaSerializer, 
    ServicioSerializer, 
    BarberoSerializer, 
    ClienteSerializer
)



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
        responses={200:openapi.Response('Servicio',ServicioSerializer)}
    )
    def get(self, request):
        obj = Servicio.objects.all()
        serializer = ServicioSerializer(instance = obj, many=True)
        return Response(serializer.data)



class clientes(APIView):
    parser_classes = (JSONParser,)

    def get(self, request):
        obj = Cliente.objects.all()
        serializer = ClienteSerializer(instance = obj, many=True)
        return Response(serializer.data)


    @swagger_auto_schema( 
        operation_description="Autentica usuarios",
        responses={200:"Usuario autenticado correctamente"},
        request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT, 
        properties={'user':openapi.Schema(description="Cédula o correo del usuario", type=openapi.TYPE_STRING),
                    'password':openapi.Schema(description="Contraseña del usuario", type=openapi.TYPE_STRING)
        }
    ))
    def post(self, request, format=None):

        userName = None
        password = None
        
        try:
            userName = request.data['user']
            password = request.data['password']            
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        if Cliente.objects.filter(userName=userName, password=password).exists():
            return Response(status=status.HTTP_200_OK)

        return Response(status=status.HTTP_404_NOT_FOUND)
        

class registro(APIView):
    parser_classes = (JSONParser,)

    @swagger_auto_schema( 
        operation_description="Crea un usuario",
        responses={200:"Usuario creado correctamente"},
        request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT, 
        properties={'username':openapi.Schema(description="Cédula o correo del usuario", type=openapi.TYPE_STRING),
                    'password':openapi.Schema(description="Contraseña del usuario", type=openapi.TYPE_STRING),
                    'cedula':openapi.Schema(description="Cédula del usuario", type=openapi.TYPE_STRING),
                    'nombre':openapi.Schema(description="Nombre y apellidos del usuario", type=openapi.TYPE_STRING)
        }
    ))

    def post(self, request, format=None):

        correo = None
        nombre = None
        cedula = None
        password = None
        
        try:
            correo = request.data['username']
            password = request.data['password']
            cedula = request.data['cedula'] 
            nombre = request.data['nombre']    

        except:
            return Response({'Hola':'nan'},status=status.HTTP_400_BAD_REQUEST)
        
        if Cliente.objects.filter(userName=correo).exists():
            return Response({'Error':'Correo ya registrado'},status=status.HTTP_409_CONFLICT)

        if Cliente.objects.filter(cedula=cedula).exists():
            return Response({'Error':'Correo ya registrado'}, status=status.HTTP_409_CONFLICT)

        Cliente(userName=correo, password=password, nombre=nombre, cedula=cedula).save()
        return Response(status=status.HTTP_201_CREATED)
        