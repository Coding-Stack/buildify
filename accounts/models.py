from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Worker(models.Model):
    wages = models.FloatField()
    prev_record = models.IntegerField()
    user = models.ForeignKey(to=User,on_delete=models.CASCADE)
    work_done = [
        ('Electrician','Electrician'),
        ('Carpenter','Carpenter'),
        ('Plumber','Plumber'),
        ('Painter','Painter'),
        ('Cons_worker','Cons_worker'),
        ('None','None'),
    ]

class Client(models.Model):
    user = models.ForeignKey(to=User,on_delete=models.CASCADE)

class Admin(models.Model):
    user = models.ForeignKey(to=User,on_delete=models.CASCADE)

class Plan(models.Model):
    client = models.OneToOneField(to=Client,on_delete=models.CASCADE)
    length = models.IntegerField()
    width = models.IntegerField()
    rooms = models.IntegerField()
    wall_thickness = models.IntegerField()
    floors = models.IntegerField()
    parking = models.BooleanField(default=True)
    status_choices = [
        ('new','new'),
        ('pending','pending'),
        ('modification','Ask For Modification'),
        ('accepted','accepted'),
        ('rejected','rejected'),
    ]
    status = models.CharField(max_length = 20, choices=status_choices, default ='new')
    drawing_plan = models.ImageField(upload_to = 'drawing',blank=True,default='default.png')
    sectional_plan = models.ImageField(upload_to = 'sectional',blank=True,default='default.png')
    floor_plan = models.ImageField(upload_to = 'floor',blank=True,default='default.png')
    elevated_plan = models.ImageField(upload_to = 'elevated',blank=True,default='default.png')

class Construction(models.Model):
    client = models.ForeignKey(to=Client,on_delete=models.CASCADE)
    workers = models.ForeignKey(to=Worker,on_delete=models.CASCADE)
    plan = models.OneToOneField(to=Plan,on_delete=models.CASCADE)
    status = [
        ('excavation','excavation'),
        ('foundation','foundation'),
        ('finished','finished')
    ]