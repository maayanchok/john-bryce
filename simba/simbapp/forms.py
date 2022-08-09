from django import forms

class UserForm(forms.Form):
    name = forms.CharField()
    birthdate = forms.DateField()
    email = forms.EmailField()
    password = forms.CharField()
    gender = forms.CharField()
    description = forms.CharField()