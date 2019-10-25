# All of the text in here was edited by me. 
#This file is where I defined my blog posts. 
# blog/models.py

from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User',on_delete=models.DO_NOTHING) #added DO_NOTHING in line 8 to ask terminal to overwrite the error message that was preventing me processing forward
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

def publish(self):
    self.published_date = timezone.now()
    self.save()

def __str__(self):
    return self.title
