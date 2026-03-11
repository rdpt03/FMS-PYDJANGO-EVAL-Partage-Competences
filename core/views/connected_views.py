from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from core.forms import TaskForm
from core.models import Skill, Task


#function to show skill for connected people
def skills_connected(request):
    if not request.user.is_authenticated:
        return redirect("skills_disconnected")
    #get all skills
    all_skills = Skill.objects.exclude(id__in=request.user.person.skills.values_list('id', flat=True)).order_by('name')

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

    template = "skills/list_connected.html"

    return render(request,template, {"page_skills": page_skills, "quantity_per_page":quantity_per_page,})


def user_skills(request):
    if not request.user.is_authenticated:
        return redirect("skills_disconnected")
    #get all skills
    all_skills = request.user.person.skills.all()

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

    return render(request,"skills/list_profile_skills.html", {"page_skills": page_skills, "quantity_per_page":quantity_per_page,})


def add_skill_to_profile(request,id):
    #get skill or 404
    skill = get_object_or_404(Skill, id=id)

    #associate and redirect
    request.user.person.skills.add(skill)
    return redirect("skills_connected")

def remove_skill_from_profile(request,id):
    #get skill or 404
    skill = get_object_or_404(Skill, id=id)

    #associate and redirect
    request.user.person.skills.remove(skill)
    return redirect("user_skills")


#-------------------------------TASKS-------------------------------
def ask_help(request, skill_id):
    #get skill
    skill = Skill.objects.get(id=skill_id)

    #if cliked into submit
    if request.method == "POST":
        #get form content
        form = TaskForm(request.POST)
        #if is valid
        if form.is_valid():
            #check if the timetable is busy
            start = form.cleaned_data["start_date"]
            end = form.cleaned_data["end_date"]

            conflict = Task.objects.filter(
                Q(start_date__lt=end) &
                Q(end_date__gt=start)
            ).exists()

            if conflict:
                #messages.error(request, "Ce créneau est déjà réservé.")
                messages = [{"text":"Vous avez deja une Tache dans ce creneaux", "code":"danger"}]
                return render(request, "tasks/ask_help.html", {"skill": skill, "form": form , "messages":messages})

            #get task
            task = form.save(commit=False)
            task.skill = skill #associate skill
            task.requester = request.user.person #associate requester
            task.published_date = timezone.now() #set publisher date as now
            task.save() #save into DB
            return redirect("home") #go back to #TODO my help requests
    #create form
    else:
        form = TaskForm()
    #show
    return render(request, "tasks/ask_help.html", {"skill":skill, "form": form})