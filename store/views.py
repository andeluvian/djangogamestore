from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import GameForm
from .models import Game


def index(request):
    games = Game.objects.all()
    return render(request, 'index.html', {'games': games})


@login_required
def developer_profile_page(request):
    current_user = request.user
    game = Game.objects.filter(game_owner_id=current_user.id)
    context = {'games': game,
               'user': current_user}
    return render(request, 'dev_profile.html', context)


@login_required
def add_game(request):
    if request.method == 'POST':
        form = GameForm(request.POST, request.FILES)
        if form.is_valid():
            game = form.save(commit=False)
            game.game_owner = request.user
            game.save()
            return redirect('dev_profile')
        else:
            return render(request, 'add_game.html', {'form': form})
    else:
        form = GameForm()
        context = {'form': form}
        return render(request, 'add_game.html', context)

    form = GameForm()
    context = {'form': form}
    return render(request, 'add_game.html', context)


def login(request):
    return render(request, 'login.html', {'context': 'context'})


def register(request):
    return render(request, 'register.html', {'context': 'context'})
