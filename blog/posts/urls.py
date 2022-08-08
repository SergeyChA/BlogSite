from django.urls import path
from .views import PostsListView, PostsDetailView, PostsCreateView,contacts

urlpatterns = [
    path('', PostsListView.as_view(), name='home'),
    path('contacts/', contacts, name='contacts'),
    path('post/<int:pk>', PostsDetailView.as_view(), name='post'),
    path('post/create', PostsCreateView.as_view(), name='post_create'),

]