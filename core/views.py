from django.core.paginator import Paginator
from django.shortcuts import render

from core.models import Skill

# Create your views here.
def home(request):
    return render(request, 'base_disconnected.html')


def skills(request):
    #get all skills
    all_skills = Skill.objects.all().order_by('name')

    print(Skill.objects.all().order_by('name'))
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

    return render(request, "disconnected_pages/skills_list.html", {"page_skills": page_skills, "quantity_per_page":quantity_per_page,})