from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic, Webpage, AccessRecord

def index(request):
    return HttpResponse("django is fun")

def index_2(request):
    return HttpResponse("<h1> Django is fun</h1>")

