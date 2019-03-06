from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from django.contrib import admin

app_name = 'questionnaire'
urlpatterns = [
    #premiere page du questionnaire
    path('', views.choixObjectif, name='choixObjectif'),
    path('choixObjectif', views.choixObjectif, name='choixObjectif'),
    path('choixProfil', views.choixProfil, name='choixProfil'),
    path('selectSport', views.selectSport, name='selectSport'),
    path('reponsesObjectifQuestion', views.reponsesObjectifQuestion, name='reponsesObjectifQuestion'),

    path('addObjective/<slug:objectif_id>', views.addObjective, name='addObjective'),
    path('deleteObjective/<slug:objectif_id>', views.deleteObjective, name='deleteObjective'),
    path('addSportChoice/<slug:sport_id>', views.addSportChoice, name='addSportChoice'),
    path('deleteSportChoice/<slug:sport_id>', views.deleteSportChoice, name='deleteSportChoice'),
    path('updateSexe/<slug:sexe>', views.updateSexe, name='updateSexe'),
    path('updateEnceinte/<slug:enceinte>', views.updateEnceinte, name='updateEnceinte'),
    path('updateAllaitante/<slug:allaitante>', views.updateAllaitante, name='updateAllaitante'),
    path('updateReponseObjectifQuestion/<slug:id>/<slug:value>', views.updateReponseObjectifQuestion, name='updateReponseObjectifQuestion'),

    path('giveMeQuestionsAnswered', views.giveMeQuestionsAnswered, name='giveMeQuestionsAnswered'),
    path('generateNewQuestion', views.generateNewQuestion, name='generateNewQuestion'),

]
