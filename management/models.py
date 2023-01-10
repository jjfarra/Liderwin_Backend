from django.db import models
from django.db.models import Model, CASCADE, DO_NOTHING, SET_NULL
from django.db.models import ForeignKey, OneToOneField, ManyToManyField
from django.db.models import (
    CharField,
    IntegerField,
    FloatField,
    DateTimeField,
    TimeField,
    BooleanField,
    FileField,
    UUIDField,
    DateField
)
# Used to generate URLs by reversing the URL patterns
from django.urls import reverse


# Create your models here.

class Cliente(Model):
    cedula = CharField(max_length=10, blank = False)
    nombre = CharField(max_length=100, blank = False)
    apellido = CharField(max_length=100, blank = False)
    direccion = CharField(max_length=500, blank = True)

    def __str__(self):
        return f"{self.cedula}, {self.nombre}, {self.apellido}"