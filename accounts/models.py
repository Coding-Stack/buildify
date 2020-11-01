from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Client(models.Model):
    user = models.ForeignKey(to=User,on_delete=models.CASCADE)
    def __str__(self):
        return self.user.first_name

class Admin(models.Model):
    user = models.ForeignKey(to=User,on_delete=models.CASCADE)
    def __str__(self):
        return self.user.first_name

class Plan(models.Model):
    client = models.ForeignKey(to=Client,on_delete=models.CASCADE)
    length = models.IntegerField()
    width = models.IntegerField()
    rooms = models.IntegerField()
    wall_thickness = models.IntegerField()
    floors = models.IntegerField()
    parking = models.BooleanField(default=True)
    status_choices_plan = [
        ('new','New'),
        ('pending','Pending'),
        ('modification','Ask For Modification'),
        ('accepted','Accepted'),
        ('rejected','Rejected'),
    ]
    status = models.CharField(max_length = 20, choices=status_choices_plan, default ='new')
    drawing_plan = models.ImageField(upload_to = 'drawing',blank=True,default='default.png')
    sectional_plan = models.ImageField(upload_to = 'sectional',blank=True,default='default.png')
    floor_plan = models.ImageField(upload_to = 'floor',blank=True,default='default.png')
    elevated_plan = models.ImageField(upload_to = 'elevated',blank=True,default='default.png')
    def __str__(self):
        return 'Plan by '+str(self.client)


class Material(models.Model):
    name = models.CharField(max_length=100)
    type_choices = [
        ('Cement','Cement'),
        ('Steel','Steel'),
        ('Sanitary_ware','Sanitary_ware'),
        ('Sand','Sand'),
        ('Aggregate','Aggregate'),
        ('Tiles','Tiles'),
        ('CP_Fitting','CP_Fitting'),
        ('Paints','Paints'),
        ('Other','Other'),
    ]
    material_type = models.CharField(max_length=20,choices=type_choices,default='Other')
    cost = models.IntegerField()
    material_img = models.ImageField(upload_to='material',default='default.png')
    def __str__(self):
        return self.name


class Construction(models.Model):
    client = models.ForeignKey(to=Client,on_delete=models.CASCADE)
    plan = models.OneToOneField(to=Plan,on_delete=models.CASCADE)
    status_choices_const = [
        ('excavation','excavation'),
        ('foundation','foundation'),
        ('finished','finished'),
    ]
    status = models.CharField(max_length=20,choices=status_choices_const,default='excavation')
    materials = models.ManyToManyField(to=Material,blank=True)
    excavation_img = models.ImageField(upload_to='construction',default='default.png')
    foundation_img = models.ImageField(upload_to='construction',default='default.png')
    finished_img = models.ImageField(upload_to='construction',default='default.png')
    estimated_cost = models.IntegerField(default=2000000)
    def __str__(self):
        return 'construction by'+str(self.client)

class Worker(models.Model):
    wage = models.FloatField(blank=True,null=True,default=0)
    prev_record = models.IntegerField()
    user = models.ForeignKey(to=User,on_delete=models.CASCADE)
    construction = models.ForeignKey(to=Construction, blank=True,null=True,on_delete=models.CASCADE)
    work_done_choices = [
        ('Electrician','Electrician'),
        ('Carpenter','Carpenter'),
        ('Plumber','Plumber'),
        ('Painter','Painter'),
        ('Cons_worker','Cons_worker'),
        ('None','None'),
    ]
    work_done = models.CharField(max_length=100,choices=work_done_choices,default='None')
    def __str__(self):
        return self.user.first_name


def isAdmin(user):
    if Admin.objects.filter(user=user).first():
        return True
    else:
        return False