from django.urls import path

from . import views

app_name = 'nutridelta'
urlpatterns = [
    path('', views.index, name='Index'),
    path('MyTest', views.MyTest, name='MyTest'),
    
    
    
]
