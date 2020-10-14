from django.urls import path
from .views import PlantListView, SinglePlantView

urlpatterns = [
    path('', PlantListView.as_view()),
    path('<int:pk>/', SinglePlantView.as_view()),
]