from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    orders = models.ManyToManyField('self', related_name='orders_made', symmetrical=False, blank=True)

    def __str__(self):
      return f'{self.first_name} {self.last_name}'