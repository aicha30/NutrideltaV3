from django import forms
from .models import Choice, Question

class addChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = '__all__'

class addQuestionForm(forms.ModelForm):
	class Meta:
		model = Question
		fields = '__all__'
   
 