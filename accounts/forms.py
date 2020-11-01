from django import forms
from django.contrib.auth.models import User
from .models import Plan,Construction,Worker,Admin,Client,Material

class PlanRegistrationForm(forms.ModelForm):
  class Meta:
      model = Plan
      fields = ['length','width','rooms','wall_thickness','floors','parking']

class PlanUpdateForm(forms.ModelForm):
    class Meta:
        model = Plan
        fields = ['drawing_plan','sectional_plan','floor_plan','elevated_plan','status']

class PlanUpdateForClientForm(forms.ModelForm):
    class Meta:
        model = Plan
        fields = ['status']        

class ConstructionRegistrationForm(forms.ModelForm):
    class Meta:
        model = Construction
        fields = ['materials','estimated_cost']

class ConstructionUpdateForm(forms.ModelForm):
    class Meta:
        model = Construction
        fields = ['plan','client','materials','status','estimated_cost','excavation_img','foundation_img','finished_img']

class WorkerRegistrationForm(forms.ModelForm):
    class Meta:
        model = Worker
        fields = ['prev_record','construction']

class WorkerUpdateForm(forms.ModelForm):
    class Meta:
        model = Worker
        fields = ['wage','prev_record','construction']

class MaterialRegistrationForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['name', 'material_type', 'cost', 'material_img']

class MaterialUpdateForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['name', 'material_type', 'cost', 'material_img']

class WorkerProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name']