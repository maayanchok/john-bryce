from django import forms

class TransactionForm(forms.Form):
    name = forms.CharField()
    amount = forms.IntegerField()
    date = forms.DateField()
    category = forms.CharField()
