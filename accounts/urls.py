from django.urls import path
from django.conf.urls import url

from .views import index,login,signup,signin,home,register

urlpatterns = [
    path('', index),
    path('login',login,name='login'),
    path('signup',signup,name='signup'),
    path('home',home,name='home'),
    path('register',register),
    path('signin',signin)
]