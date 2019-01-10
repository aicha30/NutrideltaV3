from django.contrib import admin
from django.db import models
from .models import *
from import_export.admin import ImportExportModelAdmin
from import_export import resources

# Create your models here.

# @admin.register(MicroNutriment)
# class AdminMicroNutriment(ImportExportModelAdmin):
#     pass
class ObjectifResource(resources.ModelResource):
    class Meta:
        model = Objectif
        fields = ('name')

@admin.register(Objectif)
class ObjectifAdmin(ImportExportModelAdmin):
    resource_class = ObjectifResource




# @admin.register(MicroQuestion)
# class AdminMicroQuestion(ImportExportModelAdmin):
#     pass

@admin.register(ObjectifChoice)
class AdminObjectifChoice(ImportExportModelAdmin):
    pass
