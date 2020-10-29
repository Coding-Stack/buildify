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
        fields = ['client','workers']
