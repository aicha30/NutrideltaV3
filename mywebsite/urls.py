from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url




urlpatterns = [
	path('', include('nutridelta.urls')),
   path('questionnaire/', include('questionnaire.urls'), name="questionnaire"),
   path('admin/', admin.site.urls, name="admin"),
   path('accounts/', include('accounts.urls')),



]