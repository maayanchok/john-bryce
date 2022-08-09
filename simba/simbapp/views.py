from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from ipware import get_client_ip

# Create your views here.
def index(request):
    return render(request, "authentication/index.html")

def register(request):

    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        new_user = User.objects.create_user(username, email, pass1)
        new_user.first_name = fname
        new_user.last_name = lname
        new_user.ip = get_client_ip(request)

        new_user.save()

        messages.success(request, "You account has been successfully created.")

        return redirect('http://127.0.0.1:8000/signin/')
    
    return render(request, "authentication/register.html")


def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)
        if user is not None:
            login(request,user)
            fname = user.first_name
            return render(request, "authentication/index.html", { 'fname' : fname})
        else:
            messages.error(request, "The credentials aren't valid")
    
    return render(request, "authentication/signin.html")

def signout(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect ('http://127.0.0.1:8000/')

def homepage(request):
    return render(request, "homepage.html")


def map(request):
    return render(request, "maps.html")

def chat(request):
    return HttpResponse("chat")

def search(request):
    
    return render(request, "get_location.html")

def settings(request):
    return HttpResponse("settings")

