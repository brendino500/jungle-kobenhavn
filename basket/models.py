from django.db import models

# Create your models here.
class Basket(models.Model):
  plant = models.ForeignKey(
    'plants.plant',
    related_name='User_orders',
    on_delete=models.CASCADE
  )
  user = models.ForeignKey(
    'jwt_auth.User',
    related_name='User_orders',
    on_delete=models.CASCADE
  )

  def __str__(self):
    return f'Basket {self.id} - Plant {self.plant}'