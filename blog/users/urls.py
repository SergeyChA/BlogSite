from django.urls import path
from .views import register, profile
from django.contrib.auth import views


urlpatterns = [
    path('registration/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('login/', views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('pass_reset/', views.PasswordResetView.as_view(template_name='users/pass_reset.html'), name='pass_reset'),
    path('password_reset_confirm/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(template_name='users/reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset_done/', views.PasswordResetDoneView.as_view(template_name='users/reset_done.html'), name='password_reset_done'),
    path('password_reset_complete/', views.PasswordResetCompleteView.as_view(template_name='users/reset_complete.html'), name='password_reset_complete'),
]
