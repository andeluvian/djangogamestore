from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode

from .forms import UserLoginForm, UserRegistrationForm
from .tokens import account_activation_token


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
        user.is_active = False
        user.save()
        current_site = get_current_site(request)
        subject = 'Activate Your JavaScript GameStore Account'
        message = render_to_string('authentication/account_activation_email.html', {
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
            'token': account_activation_token.make_token(user),
        })
        user.email_user(subject, message)
        return redirect('account_activation_sent')

        # password = form.cleaned_data.get('password')
        # user.set_password(password)
        # new_user = authenticate(username=user.username, password=password)
        # login(request, new_user)
        # if next:
        #     return redirect(next)
        # return redirect('/')
    context = {
        'form': form
    }
    return render(request, "registration/register.html", context)


def account_activation_sent(request):
    return render(request, 'authentication/account_activation_sent.html', {'context': 'context'})


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        return redirect('index')
    else:
        return render(request, 'authentication/account_activation_invalid.html')


# Email activate feature
# source: https://simpleisbetterthancomplex.com/tutorial/2017/02/18/how-to-create-user-sign-up-view.html