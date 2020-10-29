from django.urls import path
from django.conf.urls import url

from .views import index,login,signup,logout,signin,home,register

urlpatterns = [
    path('', index),
    path('login',login,name='login'),
    path('signup',signup,name='signup'),
    path('home',home,name='home'),
    path('register',register,name='register'),
    path('signin',signin,name='signin'),
    path('logout',logout,name='logout')
]