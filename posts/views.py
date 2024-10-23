from django.shortcuts import render, redirect
from django.http import HttpResponse
from posts.models import Post
from posts.forms import PostForm, PostForm2
import random

def test_view(request):
    return HttpResponse(random.randint(1,100))

def main_page(request):
    if request.method == 'GET':
        return render(request, 'base.html')

def list_view(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        return render(request, 'post_list.html', context={'posts':posts})

def detail_view(request, post_id):
    if request.method == 'GET':
        post = Post.objects.get(id=post_id)
        return render(request, 'post_detail.html', context={'post':post})

def post_create_view(request):
    if request.method == 'GET':
        form = PostForm2()
        return render(request, 'post_create.html', context={'form':form})
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if not form.is_valid():
            return render(request, 'post_create.html', context={'form':form})
        form.save()
        return redirect('/posts/')


