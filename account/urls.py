from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


app_name = 'account'
urlpatterns=[
	path('register', views.register, name='register'),
    path('login', views.loginMeplease, name='login'),
    path('logout', views.deco, name='logout'),
    ]