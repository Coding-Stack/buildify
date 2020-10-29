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
    length = models.IntegerField()
    width = models.IntegerField()
    rooms = models.IntegerField()
    wall_thickness = models.IntegerField()
    floors = models.IntegerField()
    parking = models.BooleanField(default=True)
    drawing_plan = models.ImageField(upload_to = './Drawing',blank=True)
    sectional_plan = models.ImageField(upload_to = './Sectional',blank=True)
    floor_plan = models.ImageField(upload_to = './Floor',blank=True)
    elevated_plan = models.ImageField(upload_to = './Elevated',blank=True)

class Construction(models.Model):
    client = models.OneToOneField(to=Client,on_delete=models.CASCADE)
    workers = models.ForeignKey(to=Worker,on_delete=models.CASCADE)
    plan = models.OneToOneField(to=Plan,on_delete=models.CASCADE)
    status = [
        ('excavation','excavation'),
        ('foundation','foundation'),
        ('finished','finished')
    ]