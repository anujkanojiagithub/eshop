from django.shortcuts import render, redirect
from store.models.customer import Customer
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from django.views import View


class Login(View):
    def get(self,request):
        return render(request,'login.html')

    def passMatching(self,obj,password):
        return check_password(password,obj.password)

    def post(self,request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        if  not Customer.objects.filter(email=email).exists():
            messages.error(request,'Email Does Not Exists')
            return render(request,'login.html')
        else:
            customerObj = Customer.getCustomerByEmail(email=email)
            if self.passMatching(customerObj,password):
                request.session['customer'] = Customer.objects.filter(email=customerObj.email).values()[0]
                print(request.session.get('customer')['email'])
                return redirect('index')
            else:
                messages.error(request,'Email and password does not match.')
                return render(request,'login.html')

def logout(request):
    request.session.clear()
    return redirect('login')