#This file adds, edits and deletes posts via the admin url.
# blog/admin.py

from django.contrib import admin
from .models import Post, Comment

admin.site.register(Post) #makes my model visible on the admin page
admin.site.register(Comment) #makes my comment visible on admin page 
