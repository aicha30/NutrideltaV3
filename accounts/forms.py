from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
	
	
	class Meta:
		model= User
		fields=('id','username','email','password1', 'password2')
		
		

class loginForm(forms.Form):
    usernameOrEmail = forms.CharField(label="Pseudo ou Email", max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)