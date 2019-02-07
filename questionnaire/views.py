from django.shortcuts import render, HttpResponseRedirect
from django.http import JsonResponse
from nutridelta.models import Objectif, ObjectifChoice, ReponseProfil, SportChoice, Sport, Regime
from nutridelta.functions import *
from nutridelta.forms import TestForm
from django.views.decorators.csrf import csrf_exempt
import logging
import json

app_name = 'questionnaire'
# Create your views here.
progress_bar_levels = [20, 40, 60, 80, 100]
questionnaire_structure = ['nutridelta:index','questionnaire:choixObjectif','questionnaire:choixProfil','questionnaire:selectSport','questionnaire:selectSport']


def choixObjectif(request):
    step = 1
    prev_url = questionnaire_structure[step - 1]
    next_url = questionnaire_structure[step + 1]
    progress_bar_width = progress_bar_levels[step]

    listeObjectives = Objectif.objects.all()
    title= "Choix de vos objectifs"
    user_id = giveMeUserId(request)
    userObjectives = ObjectifChoice.objects.filter(user_id = giveMeUserId(request) )
    specificTemplateQuestionnaire ='questionnaire/choixObjectif.html'
    return render(request, app_name+'/questionnaire.html', locals())


def choixProfil(request):
    step = 2
    prev_url = questionnaire_structure[step - 1]
    next_url = questionnaire_structure[step + 1]
    progress_bar_width = progress_bar_levels[step]


    title = "Informations essentielles"
    user_id = giveMeUserId(request)
    rep_profil_user, created = ReponseProfil.objects.get_or_create(user_id = user_id)
    list_regime = Regime.objects.all()
    if created:
        rep_profil_user.save()

    if request.method == 'POST':
        form = TestForm(request.POST)
        if form.is_valid():
            taille = form.cleaned_data.get('taille')
            poid = form.cleaned_data.get('poid')
            age = form.cleaned_data.get('age')
            regime = form.cleaned_data.get('regime')

            rep_profil_user.poid = poid
            rep_profil_user.taille = taille
            rep_profil_user.age = age

            if regime:
                rep_profil_user.regime = regime

            rep_profil_user.save()
            return HttpResponseRedirect('selectSport')

    else:
            form = TestForm()

    specificTemplateQuestionnaire = 'questionnaire/choixProfil.html'
    user_id = giveMeUserId(request)
    range_taille = range(0, 200)
    range_poid = range(0, 200)
    range_age = range(0, 200)

    return render(request, app_name+'/questionnaire.html', locals())


def selectSport(request):
    step = 3
    prev_url = questionnaire_structure[step - 1]
    next_url = questionnaire_structure[step + 1]
    progress_bar_width = progress_bar_levels[step]

    title = "Activité sportive"
    user_id = giveMeUserId(request)
    userSport = SportChoice.objects.filter(user_id= user_id)
    sportAlreadyTakenId=[]
    for elem in userSport:
        sportAlreadyTakenId.append(elem.sport.id)
    listSports = Sport.objects.exclude(id__in=sportAlreadyTakenId)
    specificTemplateQuestionnaire = 'questionnaire/selectSport.html'
    return render(request, app_name + '/questionnaire.html', locals())



@csrf_exempt
def updateSexe(request, sexe):
    user_id = request.session['session_id']
    if sexe=='True':
        newSexe=True
    else:
        newSexe=False
    rep_profil_user= ReponseProfil.objects.get(user_id=user_id)
    rep_profil_user.sexe = newSexe
    rep_profil_user.save()
    return JsonResponse({"t": "t"})

@csrf_exempt
def updateEnceinte(request, enceinte):
    user_id = request.session['session_id']
    if enceinte=='enceinte_True':
        new_enceinte=False
    else:
        new_enceinte=True
    rep_profil_user= ReponseProfil.objects.get(user_id=user_id)
    rep_profil_user.enceinte = new_enceinte
    rep_profil_user.save()
    return JsonResponse({"t": "t"})


@csrf_exempt
def updateAllaitante(request, allaitante):
    user_id = request.session['session_id']
    if allaitante=='allaitante_True':
        new_allaitante=False
    else:
        new_allaitante=True
    rep_profil_user= ReponseProfil.objects.get(user_id=user_id)
    rep_profil_user.allaitante = new_allaitante
    rep_profil_user.save()
    return JsonResponse({"t": "t"})


@csrf_exempt
def addSportChoice(request, sport_id):
        user_id = request.session['session_id']
        test, created = SportChoice.objects.get_or_create(user_id=user_id, sport_id=sport_id)
        if created:
            test.save()
        return JsonResponse({"t": "t"})


@csrf_exempt
def deleteSportChoice(request, sport_id):
    user_id = request.session['session_id']
    SportChoice.objects.filter(user_id = user_id, sport_id = sport_id).delete()
    return JsonResponse({"t": "t"})

@csrf_exempt
def addObjective(request, objectif_id):
        user_id = request.session['session_id']
        test, created=ObjectifChoice.objects.get_or_create(user_id=user_id, objectif_id=objectif_id)
        if created:
            test.save()
        return JsonResponse({"t": "t"})

@csrf_exempt
def deleteObjective(request, objectif_id):
    user_id = request.session['session_id']
    ObjectifChoice.objects.filter(user_id = user_id, objectif_id=objectif_id).delete()
    return JsonResponse({"t": "t"})










