from django.db import models
from .customer import Customer
from .product import Product

class Order(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL,blank=True,null=True)
    is_complete = models.BooleanField(default=False, null=True,blank=False)
    date = models.DateTimeField(auto_now_add=True)
    
    # again no need for this function use manager for this
    @staticmethod
    def get_order(user_id):
        try:
            order =  Order.objects.get(customer_id=user_id,is_complete=False)
        except Order.DoesNotExist: # This is not correct way use ObjectDoesNotExists Exception class.
            order = None
        return order
    
    # you use @property decorator and use OrderItems.objects.aggregate() it is much faster than this.
    def cart_total(self):
        orderitem = self.orderitem_set.all()
        cart= [i.item_total() for i in orderitem]
        total_cart = sum(cart)
        return total_cart

    def cart_count(self):
        orderitem = self.orderitem_set.all()
        cart= [i.item_total() for i in orderitem]
        length = len(cart)
        return length




    # @staticmethod
    # def get_items(user_id):
    #     try:
    #         order =  Order.objects.get(customer_id=user_id,is_complete=False)
    #         orderitem = Order.orderitem_set.filter(product_id=prod_id).exists()
    #         if orderitem:

    #     except Order.DoesNotExist:
    #         order = None
        
        

class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.SET_NULL,blank=True,null=True)
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,blank=True,null=True)
    quantity = models.IntegerField(default=0,blank=True,null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    
    #you can use @property here then you don't need to call it as a function.
    def item_total(self):
        return self.product.price * self.quantity
