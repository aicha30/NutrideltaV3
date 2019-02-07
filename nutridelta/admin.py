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

@admin.register(Sport)
class SportAdmin(ImportExportModelAdmin):
    pass

@admin.register(SportChoice)
class SportChoiceAdmin(ImportExportModelAdmin):
    pass

@admin.register(Profile)
class ProfileAdmin(ImportExportModelAdmin):
    pass

@admin.register(Regime)
class ProfileAdmin(ImportExportModelAdmin):
    pass


@admin.register(ReponseProfil)
class ReponseProfilAdmin(ImportExportModelAdmin):
    pass


@admin.register(ObjectifQuestion)
class ObjectifQuestion(ImportExportModelAdmin):
    pass

@admin.register(ReponsesObjectifQuestion)
class ReponsesObjectifQuestionAdmin(ImportExportModelAdmin):
    pass



# @admin.register(MicroQuestion)
# class AdminMicroQuestion(ImportExportModelAdmin):
#     pass

@admin.register(ObjectifChoice)
class AdminObjectifChoice(ImportExportModelAdmin):
    pass
