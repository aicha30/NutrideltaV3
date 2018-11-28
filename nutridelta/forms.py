from django import forms
from .models import Aliment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class form_aliment(forms.ModelForm):
    class Meta:
        model = Aliment
        fields = '__all__'


class SignUpForm(UserCreationForm):
	class Meta:
		model= User
		fields=('username','email','password1', 'password2',)



class loginForm(forms.Form):
    usernameOrEmail = forms.CharField(label="Pseudo ou Email", max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)