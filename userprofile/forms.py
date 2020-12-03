
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.forms import User
from django import forms

class CustomAuthenticationForm(AuthenticationForm):
    pass

class CustomUserSignupForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = (
                "username",
                "email",
                "password1",
                "password2",
            )
