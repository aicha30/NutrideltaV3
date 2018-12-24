from django.shortcuts import render
from django.http import JsonResponse
from nutridelta.models import Objectif, ObjectifChoice
import logging
import json

app_name = 'questionnaire'
# Create your views here.
def index(request):
    return render(request, 'index.html', locals())

def choixObjectif(request):
    listeObjectives=Objectif.objects.all()
    userObjectives=ObjectifChoice.objects.filter(user_id=request.session['session_id'])
    return render(request, app_name+'/choixObjectif.html', locals())

def addObjective(request,objectif_id):
        if request.method=='POST' and request.is_ajax():
                user_id=request.session['session_id']
                ObjectifChoice(user_id=user_id, objectif_id=objectif_id).save()
                return JsonResponse({"t":"t"})

def deleteObjective(request,objectif_id):
        user_id=request.session['session_id']
        ObjectifChoice.objects.filter(user_id=user_id, objectif_id=objectif_id).delete()
        return JsonResponse({"t":"t"})