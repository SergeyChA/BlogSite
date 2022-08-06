from django.urls import path
from .views import register, profile
from django.contrib.auth import views

urlpatterns = [
    path('registration/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('login/', views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    

]