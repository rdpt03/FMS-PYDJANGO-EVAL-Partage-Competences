from django.contrib import admin
from django.contrib.auth.models import User
from django import forms
from .models import Person, Skill, Task


# Register your models here.

# --- Form pour user + Person ---
# --- Admin de Person ---
@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'user')
    search_fields = ('first_name', 'last_name', 'user__username')
    # Sem form custom: cria apenas campos da Person
    # Usuário deve ser criado antes no admin padrão User


# --- Admin de Skill ---
@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


# --- Admin de Task ---
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'task_type', 'skill', 'requester', 'helper', 'start_date', 'end_date')
    list_filter = ('task_type', 'skill')
    search_fields = ('title', 'description', 'requester__first_name', 'requester__last_name')

