from django.contrib.auth import (
    authenticate,
    login

)
from django.shortcuts import render

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

from .forms import UserLoginForm


def login_view(request):
    #next = request.Get.get('next')
    form = UserLoginForm(request.POST or None)
    # if form.is_valid():
    #     username = form.cleaned_data.get('username')
    #     password = form.cleaned_data.get('password')
    #     user = authenticate(username=username, password=password)
    #     login(request, user)
    #     if next:
    #         return redirect(next)
    #     return redirect('/')
    context = {
        'form': form

    }

    return render(request, "login.html", context)


# def register_view(request):
#     next = request.Get.get('next')
#     form = UserRegisterForm(request.POST or None)
#     if form.is_valid():
#         user = form.save(commit=False)
#         password = form.cleaned_data.get('password')
#         user.set_password(password)
#         user.save()
#         new_user = authenticate(username=user.username, password=passowrd)
#         login(request, new_user)
#         if next:
#             return redirect(next)
#         return redirect('/')
#     context = {
#         'form': form
#
#     }
#
#     return render(request, "register.html", context)