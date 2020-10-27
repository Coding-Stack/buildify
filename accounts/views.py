from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')

def signup(request):
    return render(request,'signup.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        username = request.POST['username']
        email = request.POST['email'] 
        password = request.POST['password'] 
        re_password = request.POST['confirm_password'] 
        if password==re_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Emails already exists')
                return redirect('signup')
            else:
                user = User.objects.create_user(first_name=first_name, password=password,email=email,username=username)
                user.save()
                auth.login(request, user)
                return redirect('home')
        else:
            messages.info(request, "Password did not Match")
            return redirect('signup')
    else:
        return render(request, 'signup.html')

def signin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            user_name = user.username
            user = auth.authenticate(username=user_name,password=password)
            if user is not None:
                auth.login(request,user)
                return redirect('home')
            else:
                messages.error(request, 'Invalid Password')
                return redirect('login')
        else:
            messages.error(request, 'Invalid Email')  
            return redirect('login')              
    else:
        return render(request, 'login.html')

def home(request):
    return render(request,'home.html')