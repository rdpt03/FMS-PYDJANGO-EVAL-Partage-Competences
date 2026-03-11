from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

from core.forms import RegisterForm
from core.models import Person


def register_view(request):
    #if post got -> create account
    if request.method == "POST":
        #get the form content
        form = RegisterForm(request.POST)
        #if is valid
        if form.is_valid():
            # Create user
            user = form.save(commit=False)
            user.email = form.cleaned_data["email"]
            user.save()

            # create the Person and connect the user
            person = Person.objects.create(
                user=user, #connect Person to User
                first_name=form.cleaned_data["first_name"],
                last_name=form.cleaned_data["last_name"],
                phone_num=form.cleaned_data.get("phone_num"),
                address=form.cleaned_data.get("address")
            )

            # login
            login(request, user)
            return redirect("home")
    #if just a normal enter on page -> show form
    else:
        form = RegisterForm()

    return render(request, "disconnected_pages/create_account.html", {"form": form})

#login TODO docstring
def login_view(request):
    #if post -> login
    if request.method == "POST":
        #get the form
        form = AuthenticationForm(request, data=request.POST)
        #if form is valid
        if form.is_valid():
            # Authenticate user
            user = form.get_user()
            login(request, user)
            return redirect("home")
    # if just a normal enter on page -> show form
    else:
        form = AuthenticationForm()
    #if already logged in -> just redirect to the right page
    if request.user.is_authenticated:
        return redirect("home")
    else:
        return render(request, "disconnected_pages/login.html", {"form": form})

#logout TODO docstring
def logout_view(request):
    logout(request)
    return redirect("login")  # redireciona para a tela de login