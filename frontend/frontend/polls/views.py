from django.shortcuts import render
from django.template import loader

from polls.models import Question

# Create your views here.
from django.http import HttpResponse

def index(request):
    jim = "jim"
    latestQuestionList = Question.objects.all() # .order_by('-pubDate')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'jim': jim,
        'lastestQuestionList': latestQuestionList,
    }
    return HttpResponse(template.render(context, request))

def detail(request, questionID):
    return HttpResponse("You're lookig at the details of question %s." % questionID)

def results(request, questionID):
    reponse = "You're looking at the results of %s."
    return HttpResponse(response % questionID)

def vote(request, questionID):
    return HttpResponse("You're voting on question %s." % questionID)

