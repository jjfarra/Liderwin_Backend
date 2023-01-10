from django.shortcuts import render
from . import models, serializers
from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.authentication import SessionAuthentication
# Create your views here.


class ClienteViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = serializers.ClienteSerializer

    def get_queryset(self):
        cliente = models.Cliente.objects.all()
        return cliente