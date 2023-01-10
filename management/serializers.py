from . import models
from rest_framework.serializers import ModelSerializer, ImageField

class ClienteSerializer(ModelSerializer):
    class Meta:
        model = models.Cliente
        fields = ('cedula', 'nombre', 'apellido', 'direccion')