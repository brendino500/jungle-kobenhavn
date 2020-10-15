from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound, PermissionDenied
from rest_framework.permissions import IsAuthenticated

from .serializers import BasketSerializer, PopulatedBasketSerializer
from .models import Basket
# from .models import Plant
# from .serializers import PlantSerializer, PopulatedPlantSerializer


class BasketListView(APIView):

  permission_classes = (IsAuthenticated, )

  # def get(self, _request):
  #   plants = Plants.objects.all()
  #   serialized_plants = PopulatedPlantSerializer(plants, many=True)
  #   return Response(serialized_plants.data, status=status.HTTP_200_OK)

  def post(self, request):
    request.data['owner'] = request.user.id
    created_basket = BasketSerializer(data=request.data)
    if created_basket.is_valid():
      created_basket.save()
      return Response(created_basket.data, status=status.HTTP_200_OK)
    return Response(created_basket.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)


class BasketDetailView(APIView):
  
  permossion_classes = (IsAuthenticated, )

  def get_basket(self, pk):
    try:
      return Basket.objects.get(pk=pk)
    except Basket.DoesNotExist:
      raise NotFound()

  def is_basket_owner(self, basket, user):
    if basket.owner.id != user.id:
      raise PermissionDenied()

  def delete(self, request, pk):
    basket_to_delete = self.get_basket(pk)
    self.is_basket_owner(basket_to_delete, request.user)
    basket_to_delete.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)