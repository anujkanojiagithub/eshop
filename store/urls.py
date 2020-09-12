from django.urls import path
from .view import home,login,signup,misc,cart,address


urlpatterns = [
    path('',home.index,name ='index'),
    path('signup',signup.Signup.as_view(),name ='signup'),
    path('login',login.Login.as_view(),name ='login'),
    path('additem',misc.AddCart.as_view(),name ='addcart'),
    path('changeQuatity',misc.changeQuatity.as_view(),name ='changeQuatity'),
    path('logout',login.logout,name ='logout'),
    path('cart',cart.Cart.as_view(),name ='cart'),
    path('address',address.Cart.as_view(),name ='address'),
]
