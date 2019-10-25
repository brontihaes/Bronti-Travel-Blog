#This file is where all the URL's are entered and linked to the HTML
from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'), #edited to extend my application and connect the html extensions I created 
    path('post/<pk>/publish/', views.post_publish, name='post_publish'), #added to enable a publish button to appear
]
