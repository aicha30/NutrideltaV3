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
from .functions import *
from django.core.mail import send_mail
app_name = 'nutridelta'


# Create your views here.



def index(request):
    send_mail(
        'Subject here',
        'Here is the message.',
        'from@example.com',
        ['benjamin.delpech66@gmail.com'],
        fail_silently=False,
    )
    user_id = giveMeUserId(request)
    return render(request, 'index.html', locals())
