from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from todolist.models import Todolist, Userprofile

class userprofileform(forms.ModelForm):
    class Meta:
        model = Userprofile
        fields = ['user', 'address']

class Todolistform(forms.ModelForm):
    class Meta:
        model = Todolist
        fields = ['name', 'title'
        , 'description', 'priority', 'status', 'Date' ]


