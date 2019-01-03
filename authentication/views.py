from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout

)


##This is old login form, test do not work
""""
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created succesfully! Login and enjoy our site!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form':form})
"""

from .forms import (
UserLoginForm,
UserRegistrationForm
)


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
    print('Hello')
    return render(request, 'login.html', context)

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
