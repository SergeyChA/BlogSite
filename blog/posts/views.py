from django.shortcuts import render
from .models import Posts
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .form import PostsCreateForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class PostsListView(ListView):
    model = Posts
    ordering = ['-pub_date']


class PostsDetailView(DetailView):
    model = Posts

   
class PostsCreateView(LoginRequiredMixin, CreateView):
    model = Posts
    form_class = PostsCreateForm

    def get_context_data(self, **kwargs):
        context = super(PostsCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Написать статью'
        context['button_submit'] = 'Опубликовать'
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        print(self.request.user)
        return super().form_valid(form)


class PostsUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Posts
    form_class = PostsCreateForm
    template_name = 'posts/posts_form.html'

    def get_context_data(self, **kwargs):
        context = super(PostsUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Редактирование статьи'
        context['button_submit'] = 'Редактировать'
        return context

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

    def form_valid(self, form):
        form.instance.author = self.request.user
        print(self.request.user)
        return super().form_valid(form)


class PostsDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Posts
    success_url = 'home'
    template_name = 'posts/posts_delete.html'
    

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def contacts(request):
    return render (request, 'posts/contacts.html')
