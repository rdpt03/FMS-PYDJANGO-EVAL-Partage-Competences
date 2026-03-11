from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Person, Skill

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(required=True)
    phone_num = forms.CharField(max_length=20, required=False)
    address = forms.CharField(max_length=200, required=False)

    class Meta:
        model = User

        fields = ["username", "email", "password1", "password2"]