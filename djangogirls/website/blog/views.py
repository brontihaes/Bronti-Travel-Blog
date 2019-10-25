#This file links the views with the HTML templates so posts are viewed within the same structure

# blog/views.py
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Post #enabled models to import posts

# Create your views here.
def post_list(request):
    posts = Post.objects.all() #added this line to enable my posts to appear on the blog.
    return render(request, 'blog/post_list.html', {'posts': posts}) #added posts: post 
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
def post_publish(request, pk): #added these command lines to add a publish button
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)
def post_remove(request, pk): #added these command lines to add a delete button
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')
