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
  
  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('core:product', kwargs={
      "pk" : self.pk
    })

  def get_add_to_basket_url(self) :
    return reverse("core:add-to-cart", kwargs={
      "pk" : self.pk
    })

  def get_remove_from_cart_url(self) :
    return reverse("core:remove-from-cart", kwargs={
      "pk" : self.pk
    })