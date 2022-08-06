from cmath import log
from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'{username}, Вы успешно зарегистрированы')
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'users/registration.html', context={'form': form})

@login_required
def profile(request):
    return render(request, 'users/profile.html')