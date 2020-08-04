from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class SignupProfile(UserCreationForm):
	class Meta:
		model = User
		fields = ['username','email','password1','password2']

class UserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username','email','first_name','last_name']

class ProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['Phone','adresse']