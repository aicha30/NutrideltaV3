from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


app_name = 'nutridelta'
urlpatterns = [
    path('', views.index, name='index'),
    
    path('test/<int:numberQuestion>', views.test, name='test'),

    path('register', views.register, name='register'),
    path('login', views.loginMeplease, name='login'),
    path('logout', views.deco, name='logout'),
    path('mytest', views.mytest, name='mytest'),
    
    
    
]
