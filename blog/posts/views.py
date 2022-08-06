from django.shortcuts import render

def home(request):
    return render (request, 'posts/home.html')


def contacts(request):
    return render (request, 'posts/contacts.html')
