from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
def index(request):
    user_count = User.objects.count()  # Only to verify the registration form works, delete later
    return render(request, 'index.html', {'user_count': user_count})


def login(request):
    return render(request, 'login.html', {'context': 'context'})

def register(request):
    return render(request, 'register.html', {'context': 'context'})
