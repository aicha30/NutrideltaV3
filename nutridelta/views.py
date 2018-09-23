from django.shortcuts import render,get_object_or_404
from django.template.response import TemplateResponse
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect
from .models import aliment
from .forms import formaliment

# Create your views here.

def index(request):
	return render(request, 'nutridelta/index.html', locals())

def MyTest(request):
	if request.method == "GET":
		form= formaliment(request.GET)

		if(form.is_valid()):

			aliment_name=request.GET['aliment_name']
			Aliment_obj = aliment.objects.filter(aliment_name=aliment_name)[:1]
			

			if not Aliment_obj:
				form.save()

			



			return render(request, 'nutridelta/MyTest.html', locals())


	

	
	return render(request, 'nutridelta/MyTest.html', locals())




