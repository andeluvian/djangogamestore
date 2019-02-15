from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core import exceptions, serializers
from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from django.views.generic import DetailView
from django.views.generic.edit import UpdateView
from django.views.decorators.csrf import csrf_exempt
from payment.models import Transaction
from .forms import GameForm
from .models import Game, Save, Highscore
from .decorators import ajax_required


def index(request):
    games = Game.objects.all()
    return render(request, 'index.html', {'games': games})


class GameDetailView(DetailView):
    model = Game
    template_name = 'detail.html'


@login_required
def library(request):
    user = request.user
    transactions = Transaction.objects.select_related('game').filter(user=user).filter(state='SUCCESS')
    return render(request, 'library.html', {'transactions': transactions})


@login_required
def user_profile(request):
    games = Game.objects.all()
    return render(request, 'user_profile.html', {'games': games})


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


def login(request):
    return render(request, 'login.html', {'context': 'context'})


def register(request):
    return render(request, 'register.html', {'context': 'context'})


class GameEditView(LoginRequiredMixin, UpdateView):
    model = Game
    fields = ['title', 'game_file', 'cover_image', 'price']
    template_name = 'game_update.html'

    # Verify that only owner of the game can update it
    def get_object(self, *args, **kwargs):
        obj = super().get_object(*args, **kwargs)
        if obj.game_owner_id != self.request.user.id:
            raise exceptions.PermissionDenied
        return obj

    def get_success_url(self):
        return reverse('game_edit', kwargs={'pk': self.object.id})


@ajax_required
@csrf_exempt
def score(request, pk):
    score = int(request.POST.get('score'))
    username = request.user.username
    obj = Game.objects.get(pk=pk)

    highscore = Highscore(username=username, score=score)
    highscore.save()

    obj.highscores.add(highscore)

    highscores = obj.highscores.all().order_by('-score')
    keep = highscores[:5]

    if highscores.count() > 5:
        highscores.exclude(pk__in=keep).delete()

    data = serializers.serialize('json', keep)

    return HttpResponse(data)


@ajax_required
@csrf_exempt
def save(request, pk):
    gameState = request.POST.get('save_state')
    user = request.user

    try:
        obj = Save.objects.filter(game__pk=pk).get(user=user)
        obj.gameState = gameState
        obj.save()
    except Save.DoesNotExist:
        game = Game.objects.get(pk=pk)
        obj = Save(game=game, user=user, gameState=gameState)
        obj.save()

    return HttpResponse("OK")


@ajax_required
@csrf_exempt
def load(request, pk):
    user = request.user
    obj = Save.objects.filter(game__pk=pk).get(user=user)
    return HttpResponse(obj.gameState)


@login_required
def game(request, pk):
    game = Game.objects.get(pk=pk)
    highscores = game.highscores.all().order_by('-score')[:5]
    args = {'user': request.user, 'game': game, 'highscores': highscores}
    return render(request, "play.html", args)


def hardcoded(request):
    return render(request, "hardcoded_game.html")
