from django.contrib.auth.models import User
from django.db import models

# Create your models here.

#skill
class Skill(models.Model):
    #typing
    name: str
    description: str

    #attributes
    name = models.CharField(max_length=50, blank=False)
    description = models.TextField()


#person class
class Person(models.Model):
    #typing
    first_name: str
    last_name: str
    phone_num: str | None
    address: str | None

    #user to be associated
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30, blank=False)
    phone_num = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)

    #from Person to Skill
    skills = models.ManyToManyField(Skill)

#tasks
class Tasks(models.Model):
    #enum
    class TaskType(models.TextChoices):
        REQUEST = "REQUEST", "Request"
        PROPOSAL = "PROPOSAL", "Proposal"

    ###   Task -> Person
    #users relations attributes
    requester = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name="tasks_requested"
    )
    helper = models.ForeignKey(
        Person,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="tasks_helping"
    )

    #attributes
    users = models.ManyToManyField(User)
    title = models.CharField(max_length=20, blank=False, null=False)
    published_date = models.DateTimeField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    #set task_type
    task_type = models.CharField(
        max_length=10,
        choices=TaskType.choices,
        default=TaskType.REQUEST
    )
