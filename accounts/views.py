from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .models import Client,Plan,Construction,Admin
from .forms import PlanRegistrationForm,PlanUpdateForm
from django.http import HttpResponse
from django.db.models import Q
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
                client = Client(user=user)
                client.save()
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
    if Client.objects.filter(user=request.user):
        curr_user = 'Client'
    elif Admin.objects.filter(user=request.user):
        curr_user ='Admin'
    elif Worker.objects.filter(user=request.user):
        curr_user = 'Worker'
    return render(request,'home.html',{'curr_user':curr_user})

def logout(request):
    auth.logout(request)
    return redirect('/')

def new_plan(request):
    if(request.method =='POST'):
        form = PlanRegistrationForm(request.POST)
        if form.is_valid():
            length = form.cleaned_data['length']
            width = form.cleaned_data['width']
            rooms = form.cleaned_data['rooms']
            wall_thickness = form.cleaned_data['wall_thickness']
            floors = form.cleaned_data['floors']
            parking = form.cleaned_data['parking']
            client = Client.objects.filter(user=request.user)
            plan = Plan(length=length,width=width,rooms=rooms,wall_thickness=wall_thickness,floors=floors,parking=parking,client=client)
            plan.save()
            return HttpResponse('Thank you!!Our team will shortly design the best plan suited for you')
        else:
            form = PlanRegistrationForm()
    else:
        form = PlanRegistrationForm()
    return render(request, 'new_plan.html', {'form':form})

def get_plan(request, status):
   plans = Plan.objects.filter(Q(status = status),client = Client.objects.get(user=request.user) )
   return render(request,'get_plans.html',{'plans':plans})
   
def update_plan(request,id):
    plan = Plan.objects.get(id=id)
    if request.method == 'POST':
        plan = Plan.objects.get(id=request.POST.get('plan_id', None))
        form = PlanUpdateForm(request.POST,request.FILES,instance=plan)
        print(request.POST.get('plan_id'))
        if form.is_valid():
            form.save()
            messages.success(request,f'Plan is updated successfully')
        else:
            form = PlanUpdateForm(instance=plan)
    else:
        form = PlanUpdateForm(instance = plan)
    return render(request,'update_plan.html',{'form':form, 'id':id})