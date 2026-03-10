from django.contrib import admin
from django.contrib.auth.models import User
from django import forms
from .models import Person, Skill, Task


# Register your models here.

# --- Form pour user + Person ---
class PersonCreationForm(forms.ModelForm):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField(required=False)

    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'phone_num', 'address', 'skills']

    def save(self, commit=True):
        # create User before using core Django
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password'],
            email=self.cleaned_data.get('email', '')
        )
        # Save user and associate to User
        person = super().save(commit=False)
        person.user = user
        if commit:
            person.save()
            self.save_m2m()  # save ManyToManyField skills
        return person
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

