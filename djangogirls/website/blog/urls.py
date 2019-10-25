#Line 8 was edited to extend my application and connect the html extensions I created 
#This command was then linked in blog.views and imported to my URL
from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]
