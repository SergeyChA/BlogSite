from django.urls import path
from . import views
from django.views.decorators.cache import cache_page


urlpatterns = [
    path('', cache_page(60)(views.PostsListView.as_view()), name='home'),
    path('contacts/', views.ContactsFofmView.as_view(), name='contacts'),
    path('post/<int:pk>/', views.PostsDetailView.as_view(), name='post'),
    path('post/create/', views.PostsCreateView.as_view(), name='post_create'),
    path('post/update/<int:pk>/', views.PostsUpdateView.as_view(), name='post_update'),
    path('post/delete/<int:pk>/', views.PostsDeleteView.as_view(), name='post_delete'),
    path('author/<str:username>/', views.AuthorPostListView.as_view(), name='post_author'),
    path('comment/update/<int:pk>', views.CommentsUpdateView.as_view(), name='comment_update'),
    path('comment/delete/<int:pk>', views.CommentsDeleteView.as_view(), name='comment_delete'),
]
