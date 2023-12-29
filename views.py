# my_app/views.py

from django.shortcuts import render
from .models import Post  # замените на вашу модель

def news_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'news_list.html', {'posts': posts})

def post_detail(request, post_id):
    post = Post.objects.get(pk=post_id)
    return render(request, 'post_detail.html', {'post': post})