from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostsListView.as_view(), name='home'),
    path('contacts/', views.contacts, name='contacts'),
    path('post/<int:pk>/', views.PostsDetailView.as_view(), name='post'),
    path('post/create/', views.PostsCreateView.as_view(), name='post_create'),
    path('post/update/<int:pk>/', views.PostsUpdateView.as_view(), name='post_update'),
    path('post/delete/<int:pk>/', views.PostsDeleteView.as_view(), name='post_delete'),
    path('author/<str:username>/', views.AuthorPostListView.as_view(), name='post_author'),


]