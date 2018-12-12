from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.contrib import admin

app_name = 'nutridelta'
urlpatterns = [
    path('', views.index, name='index'),
    
    path('test/<int:numberQuestion>', views.test, name='test'),

  
    path('mytest', views.mytest, name='mytest'),
    
    
    
]
