from dataclasses import fields
from rest_framework import serializers
from cadastros import models

class CadastrosSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cadastros
        fields = ('users', 'password','nascimento')