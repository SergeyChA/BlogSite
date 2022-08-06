from django.shortcuts import render
from .models import Posts

def home(request):
    posts = Posts.objects.all()
    return render (request, 'posts/home.html', context = {'posts': posts})


def contacts(request):
    return render (request, 'posts/contacts.html')
