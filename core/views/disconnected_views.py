
from django.core.paginator import Paginator
from django.shortcuts import render
from django.utils import timezone

from core.models import Skill, Task

def skills_disconnected(request):
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


def tasks_disconnected(request):
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