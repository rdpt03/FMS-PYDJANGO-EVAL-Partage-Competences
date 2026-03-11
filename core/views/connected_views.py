from django.core.paginator import Paginator
from django.shortcuts import render
from core.models import Skill

#function to show skill for connected people
def skills_connected(request):
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

    #check if logged in or not to choose template
    if request.user.is_authenticated:
        template = "skills/list_connected.html"
    else:
        template = "skills/list_disconnected.html"

    return render(request,template, {"page_skills": page_skills, "quantity_per_page":quantity_per_page,})