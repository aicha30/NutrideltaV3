from django import forms
from .models import aliment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class form_aliment(forms.ModelForm):
    class Meta:
        model = aliment
        fields = '__all__'


class SignUpForm(UserCreationForm):
	

	class Meta:
		model= User
		fields=('username','email','password1', 'password2',)


class loginForm(forms.Form):
    email = forms.EmailField(label="Email", max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)