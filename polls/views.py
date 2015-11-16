from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.I dont know how to use the template")

def test(request):
    return HttpResponse("here is a test index ")

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)