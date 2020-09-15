from django.shortcuts import render, redirect
from store.models.customer import Customer
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.views import View
# Create your views here.


# learn about django form and try to do it using that

class Signup(View):
    def get(self,request):
        return render(request, 'signup.html')
    def post(self,request):
        return self.registewrUser(request)
    def registewrUser(self,request):
        postData = request.POST
        name = postData.get('name')
        email = postData.get('email')
        password = make_password(postData.get('password'))
        mobile = postData.get('mobile')
        customer = Customer(name=name, email=email,
                            password=password, mobile=mobile)

        if self.validateUser(request, customer):
            err_dict = {'name': name, 'mobile': mobile, 'email': email}
            return render(request, 'signup.html', err_dict)
        else:
            customer.save()
            messages.success(request, 'Successfully signup!!')
            return redirect('index')

    def validateUser(self,request, obj: object):
        error = None
        if self.checkLength(obj.name):
            error = True
            messages.error(request, 'Name is invalid')

        if self.checkLength(obj.email):
            error = True
            messages.error(request, 'Email can not be empty')

        if self.checkLength(obj.password):
            error = True
            messages.error(request, 'password can not be empty')

        if len(obj.mobile) < 10:
            error = True
            messages.error(
                request, 'mobile number is empty or less the 10 digits')

        if obj.isExist():
            error = True
            messages.error(request, 'Email already exists')
        return error
    

    def checkLength(self,temp: str) -> bool:
        return len(temp) < 1




