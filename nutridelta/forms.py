from django import forms
from .models import aliment

class formaliment(forms.ModelForm):
    class Meta:
        model = aliment
        fields = '__all__'