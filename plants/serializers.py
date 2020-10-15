from rest_framework import serializers
from .models import Plant
from order.serializers import PopulatedOrderSerializer, UserSerializer

class PlantSerializer(serializers.ModelSerializer):

  class Meta:
    model = Plant
    fields = '__all__'

class PopulatedPlantSerializer(PlantSerializer):

  owner = UserSerializer()
  order = PopulatedOrderSerializer(many=True)