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

class Comment(models.Model): #added so have access to a comment section on my blog
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
    
def approved_comments(self):
    return self.comments.filter(approved_comment=True) #added to be able to approve and filter comments on my blog
