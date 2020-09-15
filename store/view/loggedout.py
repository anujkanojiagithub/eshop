from django.shortcuts import render, redirect
from store.models.customer import Customer
from django.views import View
from django.http import HttpResponse,JsonResponse
import json

class AddCart(View):
    def post(self,request):
        data =json.loads(request.body.decode('utf-8')) # noneed to this if you send json from frontend . you don't have to stringify the data in frontend
        product_id = str(data.get('proid'))
        cart = request.session.get('customer')
        return_dict = {}
        if not cart:
            request.session['customer'] = {'id':None}
            cart = request.session.get('customer')

        if 'products' in  cart:
            products = cart['products']
            if product_id in products:
                products[product_id] +=1
                return_dict['quantity'] = products[product_id]
                cart['products'] = products
                request.session['customer'] = cart

            else:
                products[product_id] =1
                return_dict['quantity'] = products[product_id]
                cart['products'] = products
                request.session['customer'] = cart


        else:
            products = {}
            products[product_id]=1
            return_dict['quantity'] = products[product_id]
            cart['products'] = products
            request.session['customer'] = cart

        print(request.session['customer'])
        return JsonResponse(return_dict)


class changeQuatity(View):
    def post(self,request):
        # request.session['user_id']=1
        user_id = request.session.get('customer')['id']
        data =json.loads(request.body.decode('utf-8'))
        product_id = str(data.get('proid'))
        action = str(data.get('action'))
        cart = request.session.get('customer')
        return_dict = {}

        if action =='inc':
            if cart:
                products = cart['products']
                if product_id in products:
                    products[product_id] +=1
                    return_dict['quantity'] = products[product_id]
                    cart['products'] = products
                    request.session['customer'] = cart
                else:
                    products[product_id] =1
                    return_dict['quantity'] = products[product_id]
                    cart['products'] = products
                    request.session['customer'] = cart
            return JsonResponse(return_dict)

        if action =='desc':
            if cart:
                products = cart['products']
                if product_id in products:
                    products[product_id] -=1
                    
                    return_dict['quantity'] = products[product_id]
                    if products[product_id] ==0:
                        del products[product_id]
                    cart['products'] = products
                    request.session['customer'] = cart

            
            return JsonResponse(return_dict)

