from django.contrib.auth.models import User
from django.db import models

# Create your models here.

#person class
class Person(models.Model):
    #user to be associated
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)

