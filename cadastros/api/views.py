from urllib import response
from rest_framework import viewsets
from cadastros.api import serializers
from cadastros import models
from django.contrib.auth.models import User

class CadastrosViewSet(viewsets.ModelViewSet):
    queryset = models.Cadastros.objects.all()
    serializer_class = serializers.CadastrosSerializer
    http_method_names = ['post', 'head', 'options']

class UsersViewSet(viewsets.ModelViewSet):
    queryset = models.Cadastros.objects.all()
    serializer_class = serializers.CadastrosSerializer
    http_method_names = ['get', 'head', 'options']