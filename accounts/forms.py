from django import forms
from django.contrib.auth.models import User
from .models import Plan,Construction,Worker,Admin,Client

class PlanRegistrationForm(forms.ModelForm):
  class Meta:
      model = Plan
      fields = ['length','width','rooms','wall_thickness','floors','parking']

class PlanUpdateForm(forms.ModelForm):
    class Meta:
        model = Plan
        fields = ['drawing_plan','sectional_plan','floor_plan','elevated_plan','status']

class ConstructionRegistrationForm(forms.ModelForm):
    class Meta:
        model = Construction
        fields = ['estimated_cost']

class ConstructionUpdateForm(forms.ModelForm):
    class Meta:
        model = Construction
        fields = ['plan','client','status','estimated_cost']

class WorkerRegistrationForm(forms.ModelForm):
    class Meta:
        model = Worker
        fields = ['wage','prev_record','construction']

class WorkerUpdateForm(forms.ModelForm):
    class Meta:
        model = Worker
        fields = ['wage','prev_record','construction']