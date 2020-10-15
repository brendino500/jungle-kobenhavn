from django.db import models

class Order(models.Model):
  ordered_at = models.DateTimeField(auto_now_add=True)
  items = models.ForeignKey(
    'plants.Plant',
    related_name= 'ordered_plant',
    on_delete= models.CASCADE
  )
  customer = models.ForeignKey(
    'jwt_auth.User',
    related_name='customer_order',
    on_delete=models.CASCADE
  )

  def __str__(self):
    return f'Order#{self.id} - Customer:{self.user}'
    