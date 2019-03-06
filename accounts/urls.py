from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


app_name = 'accounts'
urlpatterns = [
    path('register', views.register, name='register'),
    path('connexion', views.connexion, name='connexion'),
    path('logout', views.deco, name='logout'),
]
