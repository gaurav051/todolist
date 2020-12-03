from django.shortcuts import render, reverse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.contrib import messages
from userprofile.forms import CustomUserSignupForm
from django.http import HttpResponseRedirect
from django.conf import settings
from todolist.models import Userprofile

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password= password )

        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/guest/'+str(user.id)+'/')

        else:
            messages.info(request, 'Username Or Password is Incorrect')


    context = {}

    return render(request, 'login.html', context)

def register_view(request):
    form = CustomUserSignupForm()

    if request.method == 'POST':
        form = CustomUserSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get("username")
            Userprofile.objects.create(
                user = user,
            )
            messages.success(request, 'Account was created' + username)
            return redirect('/user/login')

    context = {'form': form}
    return render(request, 'register.html', context)


def user_logout_view(request):

    logout(request)

    return redirect('/user/login')