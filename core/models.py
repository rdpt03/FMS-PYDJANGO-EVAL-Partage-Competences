from django.contrib.auth.models import User
from django.db import models

# Create your models here.

#person class
class Person(models.Model):
    #user to be associated
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30, blank=False)
    phone_num = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)


#competences
class Competence(models.Model):
    users = models.ManyToManyField(User)
    name = models.CharField(max_length=20, blank=False, null=False)