from django.shortcuts import render, redirect
from django.views import View
from ..models.product import Product
from ..models.order import Order,OrderItem
import json
from django.http import JsonResponse


class Cart(View):
    def get(self,request):
        user = request.session.get('customer')
        if user :
            user_id = user['id']
            order = Order.get_order(user_id)
            cart_total = order.cart_total()
            cart_count = order.cart_count()
            prod_list = order.orderitem_set.all()
            return render(request,'cart.html',{'product_info':prod_list,'cart_total':cart_total,'cart_count':cart_count})

        else:
            return   redirect('login')

    def post(self,request):
        return_dict ={}
        user = request.session.get('customer')['id']
        body = json.loads(request.body.decode('utf-8'))
        pro_id = body['id']
        value = body['value']
        order =Order.objects.get(customer_id=user,is_complete=False)
        product = order.orderitem_set.get(product_id=pro_id)
        product.quantity += value
        return_dict['status']='200'

        if product.quantity <1:
            product.delete()
            return_dict['status']='400'
        else:
            product.save()
        return_dict['count']=product.quantity
        return_dict['product_price']=product.item_total()
        return_dict['cart_total']=order.cart_total()

        

        return JsonResponse(return_dict)
