#This file links the views with the HTML templates so posts are viewed within the same structure

# blog/views.py
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Post #enabled models to import posts
from .forms import Post, CommentForm #enable a comment form page

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
def post_draft_list(request): #added these command lines to add a draft url and button link on my blog
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html', {'posts': posts}) 
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('post_detail', pk=comment.post.pk)
