from django.shortcuts import render
from .models import Question
from django.http import Http404

# Create your views here.

from django.http import HttpResponse

def index(request):
    lastOneQuestion = Question.objects.filter(id = 1)
    context = {
        'lastOneQuestion':lastOneQuestion
    }
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    try:
        question = Question.objects.get(id = question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request,'polls/detail.html', {'question':question})

def results(request, question_id):
    return HttpResponse("You are looking at the results of question %s" % question_id)

def vote(request, question_id):
    return HttpResponse("You are voting on question %s" % question_id)