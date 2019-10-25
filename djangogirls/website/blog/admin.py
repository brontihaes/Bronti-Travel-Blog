#This file adds, edits and deletes posts via the admin url.
# Line 8 makes my model visible on the admin page
# blog/admin.py

from django.contrib import admin
from .models import Post

admin.site.register(Post)
