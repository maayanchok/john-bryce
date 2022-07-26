from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest
from expenses_api.forms import TransactionForm
from expenses_api.models import Transaction

# Create your views here.

def add(request):
    form = TransactionForm
    if request.method == "POST":
        form = TransactionForm(request.POST)
        name = form.data["name"]
        date = form.data["date"]
        category = form.data["category"]
        amount = form.data["amount"]
        new_transaction = Transaction(
            name = name,
            date = date,
            category = category,
            amount = amount
            )
        new_transaction.save()
    return render(request,'add.html', {'form':form})

def display(request):
    data = Transaction.objects.all()
    return render(request,'display.html', {'data':data})

def analysis(request):
    return HttpResponse("you're in analysis")

def index(request):
    return render(request,'homepage.html')