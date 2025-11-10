from django.contrib.auth.models import Group, User
from rest_framework import serializers
from .models import Visita 

class VisitaSerializers(serializers.HyperlinkModelSerializer):
    class Meta:
        Model= Visita
        fields= ["nombre","rut","motivo","fecha_de_visita"]

class UserSerializer(serializers.HyperlinkModelSerializer):
    class Meta:
        model= User
        fields= ["url","username","email","groups"]

class GroupSerializer(serializers.HyperlinkModelSerializer):
    class Meta:
        model=Group 
        fields =["url","name"]

