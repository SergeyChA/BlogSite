from django.shortcuts import render
from .models import Posts
from django.views.generic import ListView, DetailView, CreateView
from .form import PostsCreateForm

class PostsListView(ListView):
    model = Posts
    ordering = ['-pub_date']

class PostsDetailView(DetailView):
    model = Posts
    
class PostsCreateView(CreateView):
    model = Posts
    form_class = PostsCreateForm


    def form_valid(self, form):
        form.instance.author = self.request.user
        print(self.request.user)
        return super().form_valid(form)

    
    


def contacts(request):
    return render (request, 'posts/contacts.html')
