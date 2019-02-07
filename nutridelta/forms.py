from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)


class LoginForm(forms.Form):
    usernameOrEmail = forms.CharField(label="Pseudo ou Email", max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)

class TestForm(ModelForm):
    regime = forms.ModelChoiceField(queryset=Regime.objects.all(),
                                    to_field_name='name',
                                    empty_label="--", label="Régime alimentaire")

    class Meta:
        model = ReponseProfil
        fields = ['age', 'taille', 'poid', 'regime']






    # Sexe = forms.ChoiceField(choices=SEXE_CHOICES)
    # Enceinte = forms.ChoiceField(choices=ENCEINTE_CHOICES, widget=forms.RadioSelect(
    #     attrs={'class' : 'custom-control-input'}))
    # Allaitement = forms.ChoiceField(choices=ALLAITEMENT_CHOICES)
    # # regime = forms.ForeignKey(Regime, on_delete=models.CASCADE)
    # Alcool = forms.FloatField()
    # Cigarette = forms.FloatField()
