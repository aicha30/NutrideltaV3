from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.contrib import admin

app_name = 'nutridelta'
urlpatterns = [
    path('', views.index, name='index'),
    path('aboutUs', views.aboutUs, name='aboutUs'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('mentions_legales', views.mentions_legales, name='mentions_legales'),
]
