from django.shortcuts import render
from django.http import HttpResponse
from posts.models import Post
import random

def test_view(request):
    return HttpResponse(random.randint(1,100))

def main_page(request):
    return render(request, 'base.html')

def list_view(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', context={'posts':posts})

def detail_view(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'post_detail.html', context={'post':post})
