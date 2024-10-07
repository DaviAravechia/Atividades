# from telnetlib import STATUS
# from urllib import response
# from django import HttpResponse
# from django.shortcuts import render
# from rest_framework.decorators import api_view as api_views
# from . import serializers
# from catalogo import models

from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from . import models
from . import serializers

# Create your views here.
@api_view(['GET', 'POST', 'DELETE', 'PUT'])
def getFilme(request):
    if request.method == 'GET':
        filmes = models.Filme.objects.all()
        serializer = serializers.FilmeSerializer(filmes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
