from django.urls import path
from .view import home,login,signup,misc


urlpatterns = [
    path('',home.index,name ='index'),
    path('signup',signup.Signup.as_view(),name ='signup'),
    path('login',login.Login.as_view(),name ='login'),
    path('additem',misc.AddCart.as_view(),name ='addcart'),
    path('changeQuatity',misc.changeQuatity.as_view(),name ='changeQuatity'),
    path('logout',login.logout,name ='logout'),
]
