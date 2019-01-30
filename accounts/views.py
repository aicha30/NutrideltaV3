from django.shortcuts import render, get_object_or_404, redirect
from django.template.response import TemplateResponse
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from .forms import *
from django.contrib.auth import logout, login, authenticate, get_user_model
from django.contrib.auth.forms import UserCreationForm
from nutridelta.models import Profile

# from django.contrib.sites.shortcuts import get_current_site
# from django.utils.encoding import force_bytes, force_text
# from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
# from django.template.loader import render_to_string
# from .tokens import account_activation_token
# from django.core.mail import EmailMessage


app_name = 'accounts'


def register(request):
    user_id=request.session.get('session_id')
    if request.method == 'POST':
        custom_error = []
        next = request.POST.get('next', '/')
        form = SignUpForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            test_exist_email = User.objects.filter(email=email)
            if not test_exist_email:
                # user =form.save(commit=False)
                # user.is_active = False
                # user.save()
                # current_site = get_current_site(request)
                # mail_subject = 'Active ton compte.'
                # message = render_to_string('accounts/acc_active_email.html', {
                #     'user': user,
                #     'domain': current_site.domain,
                #     'uid':urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                #     'token':account_activation_token.make_token(user),
                # })
                # to_email = form.cleaned_data.get('email')
                # email = EmailMessage(
                #             mail_subject, message, to=[to_email]
                # )
                # email.send()
                # return HttpResponse("Veillez confirmer votre adresse mail pour compléter l'inscription")
               

                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')


                
                newUser=form.save()

                Profile(user=newUser,identifiant=request.session['session_id']).save()

                del request.session['session_id']

                # user = authenticate(username=username, password=raw_password)
                # login(request, user)
                messages.success(
                    request, 'Merci pour votre inscription, un mail de confirmation vous a été envoyé.')
                return HttpResponseRedirect(next)

            else:
                custom_error.append("adresse email déjà utilisée")

        else:
            form = SignUpForm()

    return render(request, app_name + '/signup.html', locals())


# def activate(request, uidb64, token):
#     try:
#         uid = force_text(urlsafe_base64_decode(uidb64))
#         user = User.objects.get(pk=uid)
#     except(TypeError, ValueError, OverflowError, User.DoesNotExist):
#         user = None
#     if user is not None and account_activation_token.check_token(user, token):
#         user.is_active = True
#         user.save()
#         login(request, user)
#         # return redirect('home')
#         return HttpResponse("Merci d'avoir confirmer votre email. Vous pouvez vous connecter sur votre compte.")
#     else:
#         return HttpResponse("Le lien d'activation est invalisde!")


def connexion(request):
    error = False
    custom_error = []
    # messages.error(request, 'test')

    if request.method == "POST":
        next = request.POST.get('next', '/')
        form = loginForm(request.POST)

        if form.is_valid():
            usernameOrEmail = form.cleaned_data["usernameOrEmail"]
            if '@' in usernameOrEmail:
                email_verif = True
                email = usernameOrEmail
                loginName = User.objects.get(email=email).username
            else:
                email_verif = False
                loginName = usernameOrEmail

            password = form.cleaned_data["password"]
            # Nous vérifions si les données sont correctes
            user = authenticate(username=loginName, password=password)

            if user:  # Si l'objet renvoyé n'est pas None
                login(request, user)  # nous connectons l'utilisateur
                return HttpResponseRedirect(next)
            else:  # sinon une erreur sera affichée
                if email_verif is True:
                    custom_error.append(
                        "adresse email ou mot de passe incorrect")
                else:
                    custom_error.append(
                        "nom d'utilisateur ou mot de passe incorrect")
    else:
        form = loginForm()

    return render(request, app_name + '/login.html', locals())


def deco(request):
    next = request.POST.get('next', '/')
    logout(request)
    return HttpResponseRedirect(next)
