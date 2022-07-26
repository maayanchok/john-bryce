from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest

# Create your views here.

def add(request):
    return render(request,'add.html')

def display(request):
    return HttpResponse("you're in display")

def analysis(request):
    return HttpResponse("you're in analysis")

def index(request):
    return HttpResponse("""
        <h1> Hello (name), this is your current balance (balance)</h1> 
        <a href = '/expenses/add'> add</a><p>
        <a href = '/expenses/display'> display</a><p>
        <a href = '/expenses/analysis'> analysis</a>"""
    )


