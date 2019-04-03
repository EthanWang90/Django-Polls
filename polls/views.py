from django.shortcuts import render
from .models import Question

# Create your views here.

from django.http import HttpResponse

def index(request):
    lastOneQuestion = Question.objects.filter(id = 1)
    return HttpResponse(lastOneQuestion)

def detail(request, question_id):
    return HttpResponse("You're looking at question %s" % (question_id))

def results(request, question_id):
    return HttpResponse("You are looking at the results of question %s" % question_id)

def vote(request, question_id):
    return HttpResponse("You are voting on question %s" % question_id)