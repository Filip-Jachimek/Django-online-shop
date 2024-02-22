from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # user of the store
    shipping_address = models.TextField() # shipping address of the customer