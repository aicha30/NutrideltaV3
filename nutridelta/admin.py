from django.contrib import admin
from django.db import models
from .models import *
from import_export.admin import ImportExportModelAdmin

# Create your models here.

@admin.register(MicroNutriment)
class AdminMicroNutriment(ImportExportModelAdmin):
    pass


@admin.register(Objectif)
class AdminObjectif(ImportExportModelAdmin):
    pass

@admin.register(ObjectiveQuestion)
class AdminObjectiveQuestion(ImportExportModelAdmin):
    pass


@admin.register(MicroQuestion)
class AdminMicroQuestion(ImportExportModelAdmin):
    pass
