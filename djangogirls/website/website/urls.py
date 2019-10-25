#This file is where all the URL patterns are stored to enable the site to work
#Line 6 was edited in this file as I added the inclusion of blog.urls so that Django could redirect everything to this command
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [url(r'^admin/', admin.site.urls), url(r'', include('blog.urls')),]
