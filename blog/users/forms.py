from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(
        label='Введите почту' ,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control col-6'}))
    username = forms.CharField(
        label='Введите имя' ,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control col-6'}))
    password1 = forms.CharField(
        label='Введите пароль' ,
        required=True, 
        help_text='длинна не менее 8 символов',
        widget=forms.PasswordInput(attrs={'class': 'form-control col-6'})
        )
    password2 = forms.CharField(
        label='Повторите пароль',
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control col-6'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']