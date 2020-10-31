from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .models import Client,Plan,Construction,Admin,Worker
from .forms import PlanRegistrationForm,PlanUpdateForm,ConstructionRegistrationForm,ConstructionUpdateForm,WorkerRegistrationForm,WorkerUpdateForm
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


def worker_form(request):
    return render(request,'worker_form.html')

def apply(request):
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
                prev_record = request.POST['prev_record']
                work_done = request.POST['work_done']              
                worker = Worker(user=user,prev_record=prev_record,work_done=work_done)
                worker.save()
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
    if Admin.objects.filter(user=request.user).first():
        curr_user = 'Admin'
    elif Worker.objects.filter(user=request.user).first():
        curr_user ='Worker'
    else:
        curr_user = 'Client'
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
            client = Client.objects.filter(user=request.user).first()
            plan = Plan(length=length,width=width,rooms=rooms,wall_thickness=wall_thickness,floors=floors,parking=parking,client=client)
            plan.save()
            messages.success(request,'Thank you!!Our team will shortly design the best plan suited for you')
            return render('home')
        else:
            form = PlanRegistrationForm()
    else:
        form = PlanRegistrationForm()
    return render(request, 'new_plan.html', {'form':form})

def get_plan(request, status):
   print(status)
   if status.startswith('admin'):
       isAdmin = True
       if 'new' in status:
            plans = Plan.objects.filter(Q(status='new'))
       elif 'pending' in status:
            plans = Plan.objects.filter(Q(status='pending'))
       elif 'modification' in status:
            plans = Plan.objects.filter(Q(status='modification'))
       elif 'accepted' in status:
            plans = Plan.objects.filter(Q(status='accepted'))
       else:
            plans = Plan.objects.filter(Q(status='rejected'))
   else:
       isAdmin =False
       client = Client.objects.filter(user=request.user).first()
       if client:
            plans = Plan.objects.filter(Q(status = status), client=client)
       else:
           plans = []
   return render(request,'get_plans.html',{'plans':plans,'isAdmin':isAdmin})

def update_plan(request,id):
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
        plan = Plan.objects.get(id=id)
        form = PlanUpdateForm(instance = plan)
    return render(request,'update_plan.html',{'form':form, 'id':id})


def new_construction(request, id):
    if request.method == 'POST':
        plan = Plan.objects.get(id=request.POST.get('plan_id',None))
        client = plan.client
        construction = Construction(plan=plan,client=client)
        form = ConstructionRegistrationForm(request.POST,instance=construction)
        if form.is_valid():
            construction.estimated_cost = form.cleaned_data['estimated_cost']
            construction.save()           
            messages.success(request,f'Construction Updated Successfully')
        else:
            form = ConstructionRegistrationForm(instance=construction)
    else:
        plan = Plan.objects.filter(id=id).first()
        client = plan.client
        construction = Construction(plan=plan,client=client)
        form = ConstructionRegistrationForm(instance=construction)
    return render(request,'new_construction.html',{'form':form,'id':id})

def update_construction(request, id):
    if request.method == 'POST':
        construction = Construction.objects.get(id = request.POST.get('const_id',None))
        form = ConstructionUpdateForm(request.POST,instance=construction)
        if form.is_valid():
            form.save()
            messages.success(request,f'Construction Updated Successfully')
            construction.save()
        else:
            form = ConstructionUpdateForm(instance=construction)
    else:
        construction = Construction.objects.get(id=id)
        form = ConstructionUpdateForm(instance=construction)
    return render(request,'update_construction.html',{'form':form,'id':id})



def get_construction(request, status):
   if status.startswith('admin'):
        isAdmin = True
        if 'excavation' in status:
            print(1)
            constructions = Construction.objects.filter(status='excavation')
        elif 'foundation' in status:
            constructions = Construction.objects.filter(status='foundation')
        else:
            constructions = Construction.objects.filter(status='finished')
   else:
        isAdmin = False
        client = Client.objects.filter(user=request.user).first()
        if client:
            constructions = Construction.objects.filter(client=client)
        else:
            constructions = []
   return render(request, 'get_construction.html',{'constructions':constructions,'status':status,'isAdmin':isAdmin})

def get_worker(request):
    if Admin.objects.filter(user=request.user).first():
        workers = Worker.objects.all()
    else:
        return HttpResponse('Sorry! You are not authorized to view this page')
    return render(request,'get_worker.html',{'workers':workers})

def update_worker(request, id):
    if request.method == 'POST':
        worker = Worker.objects.get(id = request.POST.get('worker_id',None))
        form = WorkerUpdateForm(request.POST,instance=worker)
        if form.is_valid():
            form.save()
            messages.success(request,f'Worker Updated Successfully')
            worker.save()
        else:
            form = WorkerUpdateForm(instance=worker)
    else:
        worker = Worker.objects.get(id=id)
        form =WorkerUpdateForm(instance=worker)
    return render(request,'update_worker.html',{'form':form,'id':id})

def get_const_worker(request, id):
    workers = Worker.objects.filter(construction=Construction.objects.get(id=id))
    return render(request,'get_const_worker.html',{'workers':workers})