from django.shortcuts import render,get_object_or_404, redirect
from django.template.response import TemplateResponse
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect
from .models import *
from .forms import form_aliment, SignUpForm, loginForm
from django.contrib.auth import logout, login, authenticate,get_user_model
from django.contrib.auth.forms import UserCreationForm




# Create your views here.

def index(request):

	return render(request, 'nutridelta/index.html', locals())

def mytest(request):
	if request.method == "GET":
		form= form_aliment(request.GET)

		if(form.is_valid()):

			aliment_name=request.GET['aliment_name']
			Aliment_obj = aliment.objects.filter(aliment_name=aliment_name)[:1]
			

			if not Aliment_obj:
				form.save()

			return render(request, 'nutridelta/MyTest.html', locals())

	return render(request, 'nutridelta/MyTest.html', locals())








def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            # user = authenticate(username=username, password=raw_password)
            # login(request, user)
            return redirect('nutridelta:index')
    else:
        form = SignUpForm()

   
    return render(request, 'nutridelta/signup.html', {'form': form})




def loginMeplease(request):
    error = False
    

    if request.method == "POST":
        next = request.POST.get('next', '/')
        form = loginForm(request.POST)
        
        if form.is_valid():
            usernameOrEmail=form.cleaned_data["usernameOrEmail"]
            if '@' in usernameOrEmail:
                email= usernameOrEmail
                loginName = User.objects.get(email=email).username
            else:
                loginName= usernameOrEmail
                
            
            
            password = form.cleaned_data["password"]
            user = authenticate(username=loginName, password=password)  # Nous vérifions si les données sont correctes
           
            
            if user:  # Si l'objet renvoyé n'est pas None
                login(request, user)  # nous connectons l'utilisateur
                return HttpResponseRedirect(next)
            else: # sinon une erreur sera affichée
                error = True
    else:
        form = loginForm()

    return render(request, 'nutridelta/login.html', locals())





def deco(request):
    next = request.POST.get('next', '/')
    logout(request)
    return HttpResponseRedirect(next)




