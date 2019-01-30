from django.shortcuts import render, get_object_or_404, redirect
from django.template.response import TemplateResponse
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from .forms import *
from django.contrib.auth import logout, login, authenticate, get_user_model
from django.contrib.auth.forms import UserCreationForm
import random
from random import randint
from django.contrib.sessions.models import Session
from django.contrib.sessions.backends.db import SessionStore

app_name = 'nutridelta'


# Create your views here.


def generate_anonymous_id():
    anonymous_have_id = False
    while anonymous_have_id is False:
        rand_id = randint(0, 100000)
        test_user_id = User.objects.filter(id=rand_id)
        if test_user_id:
            None
        else:
            user_id = rand_id
            anonymous_have_id = True
    return user_id


def index(request):

    user = request.user
    if user.is_authenticated:
        test = request.user.id
        profil=Profile.objects.get(user=test)
        user_id=profil.identifiant

    if user.is_anonymous:
        test1 = request.session.get('session_id')
        if test1:
            user_id = test1
        else:
            request.session['session_id'] = generate_anonymous_id()
            user_id = request.session['session_id']

    request.session['session_id']=user_id
    #lost when the user leave the browser
    request.session.set_expiry(0)
    
   
    return render(request, 'index.html', locals())
