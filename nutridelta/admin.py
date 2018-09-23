from django.contrib import admin
from .models import aliment


class aliment_admin(admin.ModelAdmin):
	list_display=('aliment_name','frequency')



admin.site.register(aliment, aliment_admin)

