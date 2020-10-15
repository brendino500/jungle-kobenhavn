from rest_framework import serializers

from .models import Order
from order.serializers OrderSerializer

class OrderSerializer(serializers.Serializer):

  class Meta:
    model = Order
    fields = '__all__'

# class PopulatedPlantSerializer(PlantSerializer):

#   order = OrderSerializer(many=True)