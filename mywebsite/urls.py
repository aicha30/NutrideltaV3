from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url




urlpatterns = [
	path('', include('nutridelta.urls')),
    path('polls/', include('polls.urls')),
    # path('nutridelta/', include('nutridelta.urls')),
    path('admin/', admin.site.urls),



]