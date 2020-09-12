from django.shortcuts import render, redirect
from store.models.customer import Customer
from store.models.order import Order,OrderItem
from django.views import View
from django.http import HttpResponse,JsonResponse
import json

class AddCart(View):
    def post(self,request):
        data =json.loads(request.body.decode('utf-8'))
        product_id = str(data.get('proid'))
        cart = request.session.get('customer')
        return_dict = {}
        if not cart:
            return_dict['status'] = 400
            return JsonResponse(return_dict)
        else:
            user_id = cart['id']
            obj,_ = Order.objects.get_or_create(customer_id=user_id,is_complete=False)
            print(obj)
            ord_item,_ = OrderItem.objects.get_or_create(order=obj,product_id= product_id)
            ord_item.quantity +=1
            ord_item.save()
            return_dict['quantity'] = ord_item.quantity
            return_dict['status'] = 200
            
        return JsonResponse(return_dict)


class changeQuatity(View):
    def post(self,request):
        # request.session['user_id']=1
        user_id = request.session.get('customer')['id']
        data =json.loads(request.body.decode('utf-8'))
        product_id = data.get('proid')
        value = int(data.get('value'))
        cart = request.session.get('customer')
        return_dict = {}
        if cart :
            order =Order.objects.get(customer_id=user_id,is_complete=False)
            print(order)

            ord_item = order.orderitem_set.get(product_id=product_id)
            ord_item.quantity +=value
            return_dict['quantity']=ord_item.quantity
            ord_item.save()

            if ord_item.quantity ==0:
                ord_item.delete()  
            return JsonResponse(return_dict)

