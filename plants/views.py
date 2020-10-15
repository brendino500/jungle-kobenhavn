from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound, PermissionDenied
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Plant
from .serializers import PopulatedPlantSerializer, PlantSerializer


class PlantListView(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def get(self, _request):
        plants = Plant.objects.all()
        serialized_plants = PopulatedPlantSerializer(plants, many=True)
        return Response(serialized_plants.data, status=status.HTTP_200_OK)

class PlantDetailView(APIView):

    permission_classes = (IsAuthenticatedOrReadOnly, )

    def get_plant(self, pk):
        try:
            return Plant.objects.get(pk=pk)
        except Plant.DoesNotExist:
            raise NotFound()

    def is_plant_owner(self, plant, user):
        if plant.owner.id != user.id:
            raise PermissionDenied()

    def get(self, _request, pk):
        plant = self.get_plant(pk)
        serialized_plant = PopulatedPlantSerializer(plant)
        return Response(serialized_plant.data, status=status.HTTP_200_OK)