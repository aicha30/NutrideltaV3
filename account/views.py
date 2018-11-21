from django.shortcuts import render,get_object_or_404, redirect
from django.template.response import TemplateResponse
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect

from .forms import *
from django.contrib.auth import logout, login, authenticate,get_user_model
from django.contrib.auth.forms import UserCreationForm

app_name='account'

def register(request):
    if request.method == 'POST':
        next = request.POST.get('next', '/')
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            # user = authenticate(username=username, password=raw_password)
            # login(request, user)
            return HttpResponseRedirect(next)
    else:
        form = SignUpForm()

   
    return render(request, app_name+'/signup.html', {'form': form})




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

    return render(request, app_name+'/login.html', locals())





def deco(request):
    next = request.POST.get('next', '/')
    logout(request)
    return HttpResponseRedirect(next)
