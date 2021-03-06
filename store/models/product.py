from django.db import models
from .category import Category

class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=200, default='')
    image = models.ImageField(upload_to='products/image')
    
    #again not need for these static methos youe need override manager
    @staticmethod
    def get_all_product():
        return Product.objects.all()

    def __str__(self):
        return f"{self.name} :{self.price}"

    @staticmethod
    def getProductByCat(cat_id):
        return Product.objects.filter(pk=cat_id)
