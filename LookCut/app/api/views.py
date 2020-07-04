from django.shortcuts import render
from rest_framework.parsers import JSONParser
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework.views import APIView

class hola(APIView):
    parser_classes = (JSONParser,)

    def get(self, request):

        return Response('hola')

class barberos(APIView):
    parser_classes = (JSONParser,)

    def get(self, request):

        return Response('hola')

class barberias(APIView):
    parser_classes = (JSONParser,)

    def get(self, request):

        return Response('hola')