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