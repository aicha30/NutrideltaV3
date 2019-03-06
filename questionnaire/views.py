from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.http import JsonResponse
from nutridelta.models import ReponsesObjectifQuestion, ObjectifQuestion, Objectif, ObjectifChoice, ReponseProfil, \
    SportChoice, Sport, Regime
from nutridelta.functions import *
from nutridelta.forms import TestForm
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
import logging
import json

app_name = 'questionnaire'
# Create your views here.
progress_bar_levels = [0, 10, 20, 30, 40, 50, 60]
questionnaire_structure = ['nutridelta:index', 'questionnaire:choixObjectif', 'questionnaire:choixProfil',
                           'questionnaire:selectSport', 'questionnaire:reponsesObjectifQuestion',
                           'questionnaire:reponsesObjectifQuestion']


def choixObjectif(request):
    step = 1
    prev_url = 'nutridelta:index'
    next_url = questionnaire_structure[step + 1]
    progress_bar_width = progress_bar_levels[step]

    listeObjectives = Objectif.objects.all()
    title = "Choix de vos objectifs"
    user_id = giveMeUserId(request)
    userObjectives = ObjectifChoice.objects.filter(user_id=giveMeUserId(request))
    specificTemplateQuestionnaire = 'questionnaire/choixObjectif.html'
    specificTitleQuestionnaire = 'questionnaire/titleQuestionnaire.html'
    specificBottomQuestionnaire = 'questionnaire/suivant.html'
    return render(request, app_name + '/questionnaire.html', locals())


def choixProfil(request):
    step = 2
    prev_url = questionnaire_structure[step - 1]
    next_url = questionnaire_structure[step + 1]
    progress_bar_width = progress_bar_levels[step]

    title = "Informations essentielles"
    user_id = giveMeUserId(request)
    rep_profil_user, created = ReponseProfil.objects.get_or_create(user_id=user_id)
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
    specificTitleQuestionnaire = 'questionnaire/titleQuestionnaire.html'
    specificBottomQuestionnaire = 'questionnaire/suivant.html'
    user_id = giveMeUserId(request)
    range_taille = range(0, 200)
    range_poid = range(0, 200)
    range_age = range(0, 200)

    return render(request, app_name + '/questionnaire.html', locals())


def selectSport(request):
    step = 3
    prev_url = questionnaire_structure[step - 1]
    next_url = questionnaire_structure[step + 1]

    progress_bar_width = progress_bar_levels[step]

    title = "Activité sportive"
    user_id = giveMeUserId(request)
    userSport = SportChoice.objects.filter(user_id=user_id)
    sportAlreadyTakenId = []
    for elem in userSport:
        sportAlreadyTakenId.append(elem.sport.id)
    listSports = Sport.objects.exclude(id__in=sportAlreadyTakenId)
    specificTemplateQuestionnaire = 'questionnaire/selectSport.html'
    specificTitleQuestionnaire = 'questionnaire/titleQuestionnaire.html'
    specificBottomQuestionnaire = 'questionnaire/suivant.html'
    return render(request, app_name + '/questionnaire.html', locals())


def reponsesObjectifQuestion(request):
    title = "Santé "
    user_id = giveMeUserId(request)
    page_maximum_question_number = 5

    step = 4

    prev_url = questionnaire_structure[step - 1]
    next_url = questionnaire_structure[step + 1]
    progress_bar_width = progress_bar_levels[step]

    specificTemplateQuestionnaire = 'questionnaire/reponseObjectifQuestion.html'
    specificTitleQuestionnaire = 'questionnaire/titleQuestionnaire_legende_pour_questions.html'
    specificBottomQuestionnaire = 'questionnaire/suivant2.html'
    return render(request, app_name + '/questionnaire.html', locals())


def updateReponseObjectifQuestion(request, id, value):
    user_id = giveMeUserId(request)
    if ReponsesObjectifQuestion.objects.filter(user_id=user_id, question_id=id):
        reponse = ReponsesObjectifQuestion.objects.get(user_id=user_id, question_id=id)
        reponse.value = value
        reponse.save()
    else:
        ReponsesObjectifQuestion(user_id=user_id, question_id=id, value=value).save()
    return JsonResponse({"t": "t"})


def updateSexe(request, sexe):
    user_id = giveMeUserId(request)
    if sexe == 'True':
        newSexe = True
    else:
        newSexe = False
    rep_profil_user = ReponseProfil.objects.get(user_id=user_id)
    rep_profil_user.sexe = newSexe
    rep_profil_user.save()
    return JsonResponse({"t": "t"})


def updateEnceinte(request, enceinte):
    user_id = giveMeUserId(request)
    if enceinte == 'enceinte_True':
        new_enceinte = False
    else:
        new_enceinte = True
    rep_profil_user = ReponseProfil.objects.get(user_id=user_id)
    rep_profil_user.enceinte = new_enceinte
    rep_profil_user.save()
    return JsonResponse({"t": "t"})


def updateAllaitante(request, allaitante):
    user_id = giveMeUserId(request)
    if allaitante == 'allaitante_True':
        new_allaitante = False
    else:
        new_allaitante = True
    rep_profil_user = ReponseProfil.objects.get(user_id=user_id)
    rep_profil_user.allaitante = new_allaitante
    rep_profil_user.save()
    return JsonResponse({"t": "t"})


def addSportChoice(request, sport_id):
    user_id = giveMeUserId(request)
    test, created = SportChoice.objects.get_or_create(user_id=user_id, sport_id=sport_id)
    if created:
        test.save()
    return JsonResponse({"t": "t"})


def deleteSportChoice(request, sport_id):
    user_id = giveMeUserId(request)
    SportChoice.objects.filter(user_id=user_id, sport_id=sport_id).delete()
    return JsonResponse({"t": "t"})


def addObjective(request, objectif_id):
    user_id = giveMeUserId(request)
    test, created = ObjectifChoice.objects.get_or_create(user_id=user_id, objectif_id=objectif_id)
    if created:
        test.save()
    return JsonResponse({"t": "t"})


def deleteObjective(request, objectif_id):
    user_id = giveMeUserId(request)
    ObjectifChoice.objects.filter(user_id=user_id, objectif_id=objectif_id).delete()
    return JsonResponse({"t": "t"})


def giveMeQuestionsAnswered(request):
    user_id = giveMeUserId(request)
    end = 0

    userObjectifs = ObjectifChoice.objects.filter(user_id=user_id).values_list('objectif_id', flat=True)

    questions = []
    reponses = []

    if len(ObjectifQuestion.objects.filter(objectif_id__in=userObjectifs)):




        test3 = ReponsesObjectifQuestion.objects.filter(user_id=user_id)
        test4 = test3.values_list('question_id', flat= True)
        test2 = ObjectifQuestion.objects.filter(objectif_id__in=userObjectifs, id__in = test4 )

        questions.append(list(test2.values()))
        reponses.append(list(test3.values()))
    else:

        id = None
        name = None
        objectif_name = None
        end = 1

    try:
        reponse = ReponsesObjectifQuestion.objects.filter(user_id=user_id, question=test)[0]
        reponse_value = reponse.value
    except:
        reponse_value = None

    return JsonResponse({"questions": questions, "reponses": reponses, "test":list(userObjectifs.values())})


def generateNewQuestion(request):
    user_id = giveMeUserId(request)
    objectivesUser = ObjectifChoice.objects.filter(user_id=user_id).values_list('objectif_id', flat=True)
    newQuestion = []
    myQuestion = None
    noMoreQuestion = True
    for objective in objectivesUser:
        questionsForThisObjectif = ObjectifQuestion.objects.filter(objectif_id=objective)
        reponsesQuestionsObjectivesUser = ReponsesObjectifQuestion.objects.filter(user_id=user_id,
            question_id__in=questionsForThisObjectif).values_list('question_id', flat=True)

        if reponsesQuestionsObjectivesUser.count() < 3 and questionsForThisObjectif.count() > 0:
            test = "wow"
            myQuestion = ObjectifQuestion.objects.filter(objectif_id=objective).exclude(
                id__in=reponsesQuestionsObjectivesUser)[:1]

            newQuestion.append(list(myQuestion.values()))
            noMoreQuestion = False
            break;

    return JsonResponse({"newQuestion": newQuestion, "noMoreQuestion": noMoreQuestion})
