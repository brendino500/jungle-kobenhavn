from django.db import models

# Create your models here.
class Basket(models.Model):
  plant = models.ForeignKey(
    'plants.plant',
    related_name='basket_orders',
    on_delete=models.CASCADE
  )
  ordered_date = models.DateTimeField(auto_now_add=True)
  
  # models.ForeignKey(
  #   'plants.plant',
  #   related_name='User_orders',
  #   on_delete=models.CASCADE
  # )
  user = models.ForeignKey(
    'jwt_auth.User',
    related_name='user_orders',
    on_delete=models.CASCADE
  )

  def __str__(self):
    return f'Order#{self.id} - Customer: {self.user}'
