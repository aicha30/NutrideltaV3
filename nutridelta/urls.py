from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


app_name = 'nutridelta'
urlpatterns = [
    path('', views.index, name='index'),
    
    path('register', views.register, name='register'),
    path('connexion', views.loginMeplease, name='login'),
    path('Logout', views.deco, name='logout'),
    path('mytest', views.mytest, name='mytest'),
    
    
    
]
