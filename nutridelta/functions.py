from django.shortcuts import render, get_object_or_404, redirect
from random import randint
from .models import Profile
from django.contrib.auth.models import User

def generate_anonymous_id():
    anonymous_have_id = False
    while anonymous_have_id is False:
        rand_id = randint(0, 100000)
        test_user_id = User.objects.filter(id=rand_id)
        test_profile_id = Profile.objects.filter(identifiant=rand_id)
        if test_user_id and test_profile_id:
            None
        else:
            user_id = rand_id
            anonymous_have_id = True
    return user_id



def giveMeUserId(request):
    user = request.user

    # Si l'utilisateur est authentifié
    if user.is_authenticated:
        try:
            my_profil = Profile.objects.get(user=request.user.id)
            user_id = my_profil.identifiant

        # Sinon on cree un profil
        except:
            if request.session.get('session_id'):
                new_identifiant = request.session.get('session_id')
                Profile(user=request.user.id, identifiant = request.session.get('session_id'))
            else:
                new_identifiant = generate_anonymous_id()
            Profile(user=request.user.id, identifiant=new_identifiant).save()
            user_id = new_identifiant


    # Si l'utilisateur est anonyme
    if user.is_anonymous:
        user_id = request.session.get('session_id')
    # Si il existe une variable de session, on recupere

    # Sinon on genere un id aleatoire, et on crée une variable de session 'session_id'
    if not user_id:
        request.session['session_id'] = generate_anonymous_id()
        user_id = request.session['session_id']

    request.session['session_id'] = user_id

    # lost when the user leave the browser
    request.session.set_expiry(0)


    return user_id
