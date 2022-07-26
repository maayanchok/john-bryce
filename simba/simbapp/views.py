from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homepage(request):
    return HttpResponse("homepage")

def map():
    return HttpResponse("map")

def chat():
    return HttpResponse("chat")

def search():
    return HttpResponse("search")

def settings():
    return HttpResponse("settings")

def sign_in():
    return HttpResponse("sign in")

def register():
    return HttpResponse("register")