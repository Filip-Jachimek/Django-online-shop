from django.db import models
from django.contrib.auth.models import User
from .customer import Customer
from .models import Figure


class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE) # customer associated with the cart
    products = models.ManyToManyField(Figure, through='CartProduct') # products in cart
    added_date = models.DateTimeField(auto_now_add=True) # date when products were added to the cart


class CartProduct(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE) # cart to which product belongs
    figure = models.ForeignKey(Figure, on_delete=models.CASCADE) # figure in the cart
    quantity = models.IntegerField() # quantity of the product in the cart

    