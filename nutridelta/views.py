from django.shortcuts import render,get_object_or_404, redirect
from django.template.response import TemplateResponse
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect
from .models import *
from .forms import *
from django.contrib.auth import logout, login, authenticate,get_user_model
from django.contrib.auth.forms import UserCreationForm




# Create your views here.

def index(request):

	return render(request, 'index.html', locals())

def mytest(request):
	if request.method == "GET":
		form= form_aliment(request.GET)

		if(form.is_valid()):

			aliment_name=request.GET['aliment_name']
			Aliment_obj = aliment.objects.filter(aliment_name=aliment_name)[:1]
			

			if not Aliment_obj:
				form.save()

			return render(request, 'MyTest.html', locals())

	return render(request, app_name+'MyTest.html', locals())








def test(request, numberQuestion):
    return render(request,'questions/Question1.html')