from django.db import models
from django.contrib.auth.models import User
from .models import Figure
from .customer import Customer


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE) # customer placing an order   
    products = models.ManyToManyField(Figure, through='OrderProduct') # products in order
    order_date = models.DateTimeField(auto_now_add=True) # date of order
    STATUS_CHOICES = [
        ('P', 'Pending'),
        ('R', 'In progress'),
        ('C', 'Completed'),
    ]
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    total_price = models.DecimalField(max_digits=10, decimal_places=2) 

class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE) # order to which the product belongs
    figure = models.ForeignKey(Figure, on_delete=models.CASCADE) # figure in the order
    quantity = models.IntegerField() # quantity of the product in the order