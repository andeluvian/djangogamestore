from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render

from .forms import UserLoginForm, UserRegistrationForm


def login_view(request):
    #    next = request.Get.get('next')
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect('/')

    context = {
        'form': form
    }
    return render(request, 'registration/login.html', context)


def register_view(request):
    #     next = request.Get.get('next')
    form = UserRegistrationForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        if next:
            return redirect(next)
        return redirect('/')

    context = {
        'form': form
    }
    return render(request, "register.html", context)
