from django.shortcuts import render, redirect
from .forms import UserRegisterForm, ProfileImageForm, UserUpdateForm
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
    if request.method == 'POST':
        profile_form = ProfileImageForm(request.POST, request.FILES, instance=request.user.profile)
        update_form = UserUpdateForm(request.POST, instance=request.user)
        if profile_form.is_valid and update_form.is_valid:
            profile_form.save()
            update_form.save()
            messages.success(request, 'Ваш аккаунт был изменен')
            return redirect('profile')
    else:
        profile_form = ProfileImageForm(instance=request.user.profile)
        update_form = UserUpdateForm(instance=request.user)
    return render(request, 'users/profile.html', context={'profile_form': profile_form,
                                                          'update_form': update_form})
