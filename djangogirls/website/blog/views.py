#Lines 5 and 8-12 were edited here by me.
#This file links the views with the HTML templates so posts are viewed within the same structure
# blog/views.py
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404

# Create your views here.
def post_list(request):
    return render(request, 'blog/post_list.html', {})
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
