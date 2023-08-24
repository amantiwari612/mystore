from django.urls import path
# from app1.views import data,index,productall,productfilter,login,productget
from app1.views import *
urlpatterns = [
    path('data/',data),
    path('',index,name="index1"),
    path('product-all/',productall),
    path('product-filter/<int:id>/',productfilter),
    path('login/',login,name="login"),
    path('logout/',logout,name="logout"),
    path('register/',register),
    path('product-get/<int:id>/',productget,name="productdetails"),
    path('profile/',profile,name="profile"),
    path('contactus/',contact,name="contact"),
    path('buynow/',buynow,name="Buy"),
    path('ordertable/',ordertable,name="order"),
    path('ordersucces/',ordersucess,name="ordersuccesview"),
    
]