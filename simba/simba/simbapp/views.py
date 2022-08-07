from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def homepage(request):
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

        new_user.save()

        messages.success(request, "You account has been successfully created.")

        redirect('signin/')
    else:
        return render(request, "authentication/register.html")


def signin(request):
    
    return render(request, "authentication/signin.html")

def signout(request):
    pass

def map(request):
    return HttpResponse("map")

def chat(request):
    return HttpResponse("chat")

def search(request):
    return HttpResponse("search")

def settings(request):
    return HttpResponse("settings")

