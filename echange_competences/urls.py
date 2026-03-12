"""
URL configuration for echange_competences project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    #skills
    path('skills/', views.skills_connected, name='skills_connected'),
    path('skills/user_skills/', views.user_skills, name='user_skills'),
    path('skills/add_to_profile/<int:id>/', views.add_skill_to_profile, name='add_skill_to_profile'),
    path('skills/remove_from_profile/<int:id>/', views.remove_skill_from_profile, name='remove_skill_from_profile'),

    #tasks
    path('tasks/ask_help/<int:skill_id>', views.ask_help, name='ask_help'),
    path('tasks/my_tasks', views.my_tasks, name='my_tasks'),
    path('tasks/requests', views.help_requests_tasks, name='help_requests_tasks'),
    path('tasks/accept_task/<int:task_id>', views.accept_task, name='accept_task'),
    path('tasks/helping', views.my_helping_tasks, name='my_helping_tasks'),


    path('guest/skills/', views.skills_disconnected, name='skills_disconnected'),
    path('guest/tasks/', views.tasks_disconnected, name='tasks_disconnected'),

    # login register
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout')
]
