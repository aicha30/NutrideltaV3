from django.shortcuts import render
from django.http import JsonResponse
from nutridelta.models import Objectif, ObjectifChoice, ReponseProfil
from nutridelta.functions import *
import logging
import json

app_name = 'questionnaire'
# Create your views here.




def index(request):
    listeObjectives = Objectif.objects.all()



    userObjectives = ObjectifChoice.objects.filter(user_id = giveMeUserId(request) )


    specificTemplate='questionnaire/choixObjectifTest.html'

    return render(request, app_name+'/index.html', locals())



def addObjective(request, objectif_id):
        user_id = request.session['session_id']

        test, created=ObjectifChoice.objects.get_or_create(user_id=user_id, objectif_id=objectif_id)
        if created:
            test.save()
        return JsonResponse({"t": "t"})


def deleteObjective(request, objectif_id):
    user_id = request.session['session_id']
    ObjectifChoice.objects.filter(user_id = user_id, objectif_id=objectif_id).delete()
    return JsonResponse({"t": "t"})





def choixProfil(request):
    userProfils=ReponseProfil.objects.filter(user_id=request.session['session_id'])
    return render(request, app_name+'/choixProfil.html', locals(),)




