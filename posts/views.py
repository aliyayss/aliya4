from django.shortcuts import render
from django.http import HttpResponse
import random

def test_view(request):
    return HttpResponse(random.randint(1,100))

def test_view2(request):
    return render(request, 'base.html')

