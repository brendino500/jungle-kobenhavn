from django.db import models

# Create your models here.
class Plant(models.Model):
  name = models.CharField(max_length=60)
  image = models.CharField(max_length=400)
  price = models.IntegerField()
  description = models.CharField(max_length=800)
  potDiameter = models.IntegerField()
  approxHeight = models.IntegerField()
  
  def __str__(self):
      return f'{self.name}'