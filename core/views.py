from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.utils import timezone

from core.forms import RegisterForm
from core.models import Skill, Task, Person


# Create your views here.
def home(request):
    return render(request, 'base_disconnected.html')


def skills(request):
    #get all skills
    all_skills = Skill.objects.all().order_by('name')

    #get page number
    page_num = request.GET.get('page')

    #gets quantity per page
    try:
        quantity_per_page = int(request.GET.get('quantity', 20))
        if quantity_per_page <= 0:
            quantity_per_page = 20
    except ValueError:
        quantity_per_page = 20

    #paginator
    paginator = Paginator(all_skills, quantity_per_page)
    page_skills = paginator.get_page(page_num)

    #check if logged in or not to choose template
    if request.user.is_authenticated:
        template = "skills/list_connected.html"
    else:
        template = "skills/list_disconnected.html"

    return render(request,template, {"page_skills": page_skills, "quantity_per_page":quantity_per_page,})


def tasks(request):
    # get all tasks
    all_tasks = Task.objects.all().filter(
        helper__isnull=True,
        task_type=Task.TaskType.REQUEST,
        start_date__gt=timezone.now()
    ).order_by('-published_date')

    # get page number
    page_num = request.GET.get('page')
    # gets quantity per page
    try:
        quantity_per_page = int(request.GET.get('quantity', 20))
        if quantity_per_page <= 0:
            quantity_per_page = 20
    except ValueError:
        quantity_per_page = 20

    # paginator
    paginator = Paginator(all_tasks, quantity_per_page)
    page_tasks = paginator.get_page(page_num)

    return render(request, "tasks/list.html",
                  {"page_tasks": page_tasks, "quantity_per_page": quantity_per_page, })


###################LOGIN HANDLER########################
#register TODO docstring
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