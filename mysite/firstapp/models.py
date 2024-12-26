import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib import admin

# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    
    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?",
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
    
class FirstappUser(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    country = models.CharField(max_length = 50)


class Userlog(models.Model):
    actions = [
        ('login', 'login succ'),
        ('question', 'look question list'),
        ('vote', 'Vote a question'),
        ('detail', 'view singe question info')
    ]

    user = models.ForeignKey(FirstappUser, on_delete=models.CASCADE)
    action_time = models.DateTimeField()
    action = models.CharField(choices=actions, max_length=20)







