from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    mobile = models.CharField(max_length=12)
    password = models.CharField(max_length=500)

    def isExist(self):
        return Customer.objects.filter(email=self.email)
    
    # again no need for these methods django provides managers for this purpose. If you want to write your custom filters override the manager.
    @staticmethod
    def getCustomerByEmail(email):
        return Customer.objects.get(email=email)
    @staticmethod
    def getCustomerById(id):
        return Customer.objects.get(id=int(id))

