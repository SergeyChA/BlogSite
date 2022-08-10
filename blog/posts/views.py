from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from .models import Posts, Comments
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .form import PostsCreateForm, CommentsCreateForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class PostsListView(ListView):
    model = Posts
    ordering = ['-pub_date']
    paginate_by = 10

class AuthorPostListView(ListView):
    model = Posts
    paginate_by = 10

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Posts.objects.filter(author=user).order_by('-pub_date')


class PostsDetailView(DetailView):
    model = Posts

    def get_context_data(self, **kwargs):
        context = super(PostsDetailView, self).get_context_data(**kwargs)
        comments = Comments.objects.filter(post_id=self.kwargs.get('pk')).order_by('-pub_date')
        form = CommentsCreateForm()
        context['form'] = form
        context['comments'] = comments 
        return context
    
    def post(self, request, pk):
        form = CommentsCreateForm(data=request.POST)
        form.instance.author_id = self.request.user.id
        form.instance.post_id = pk
        if form.is_valid():
            form.save()
        return redirect('post', pk)

class CommentsUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comments
    form_class = CommentsCreateForm
    template_name = 'posts/comment_form.html'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class CommentsDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comments
    template_name = 'posts/comment_delete.html'
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

    def get_success_url(self):
        return f'/post/{self.object.post_id}'
  
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
    success_url = '/'
    template_name = 'posts/posts_delete.html'
    

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def contacts(request):
    return render (request, 'posts/contacts.html')
