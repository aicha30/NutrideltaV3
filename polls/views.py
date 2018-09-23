from django.shortcuts import render,get_object_or_404
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect
from .forms import addChoiceForm, addQuestionForm
from .models import Question, Choice
from django.views import generic


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'





def addChoice(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	form = addChoiceForm(request.POST or None)
	
	
	if form.is_valid():
		
		form.save()
		envoi = True
	
	return render(request, 'polls/addChoice.html', locals())


def addQuestion(request):
	form= addQuestionForm(request.POST or None)


	if form.is_valid():
		form.save()
		envoi = True

	return render(request, 'polls/addQuestion.html', locals())






def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    choice=get_object_or_404(Choice, pk=request.POST['choice']) #same
    choice = question.choice_set.get(pk=request.POST['choice'])	#same
    choice.votes += 1
    choice.save()
    return HttpResponseRedirect(reverse('polls:index'));




class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'