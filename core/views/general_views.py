from django.shortcuts import render, redirect


def home(request):
    if request.user.is_authenticated:
        return redirect("skills_disconnected")
    else:
        return redirect("skills_connected")#TODO temporary - replace with help asked
    #return render(request, 'base_disconnected.html')