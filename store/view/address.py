from django.shortcuts import render, redirect
from django.views import View


class Cart(View):
    def get(self,request):
        return render(request,'address.html')
    def post(self,request):
        data = request.POST
        name = data['name']
        mobile = data['mobile']
        address = data['address']
        return render(request,'address.html')