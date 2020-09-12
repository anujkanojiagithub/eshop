from django.db import models
from store.models.customer import Customer
class Address(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=1000)
    mobile = models.CharField(max_length=12)