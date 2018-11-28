from django.contrib import admin
from django.db import models
from .models import *
from import_export.admin import ImportExportModelAdmin

# Create your models here.

@admin.register(Aliment)
class AdminAliment(ImportExportModelAdmin):
    pass
