from django.shortcuts import render

from . models import Game


# Create your views here.
def index(request):
    games = Game.objects.all()
    return render(request, 'index.html', {'games': games})


def login(request):
    return render(request, 'login.html', {'context': 'context'})


def register(request):
    return render(request, 'register.html', {'context': 'context'})
