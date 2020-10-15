from django.db import models

# Create your models here.
class Plant (models.Model):
  name = models.CharField(max_length=60)
  image = models.CharField(max_length=400)
  price = models.IntegerField()
  description = models.CharField(max_length=800)
  potDiameter = models.IntegerField()
  approxHeight = models.IntegerField()
  # customer = models.ForeignKey(
  #   'jwt_auth.User',
  #   related_name='customer_order',
  #   on_delete=models.CASCADE
  # )
  basket = models.ForeignKey(
    'basket.Basket',
    related_name='orders',
    on_delete=models.CASCADE
  )
  
  def __str__(self):
    return f'{self.name}'