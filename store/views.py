from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core import exceptions
from django.shortcuts import render, redirect, reverse
from django.views.generic import DetailView
from django.views.generic.edit import UpdateView
from django.views.decorators.csrf import csrf_exempt
from .forms import GameForm
from .models import Game


def index(request):
    games = Game.objects.all()
    return render(request, 'index.html', {'games': games})


class GameDetailView(DetailView):
    model = Game
    template_name = 'detail.html'


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


@csrf_exempt
def score(request):
    if request.is_ajax():



        request_data = request.POST
        score = request_data.get('Score')
        title = request_data.get('title')
        player = request.user.username
        obj = Game.objects.get(title=title)

        # update highscores
        if float(score) >= obj.Rank1pts:


            obj.Rank3pts = obj.Rank2pts
            obj.Rank3player = obj.Rank2player


            obj.Rank2pts = obj.Rank1pts
            obj.Rank2player = obj.Rank1player

            obj.Rank1pts = score
            obj.Rank1player = player
            obj.save()

        elif float(score) >= obj.Rank2pts:

            obj.Rank3pts = obj.Rank2pts
            obj.Rank3player = obj.Rank2player

            obj.Rank2pts = score
            obj.Rank2player = player
            obj.save()

        elif float(score) >= obj.Rank3pts:
            obj.Rank3pts = score
            obj.Rank3player = player
            obj.save()


        return HttpResponse("OK")




@csrf_exempt
def save(request):
    if request.is_ajax():

        request_data = request.POST
        save_State = request_data.get('save_State')
        title = request_data.get('Title')
        player = request.user.username

        try:
            objects = Save.objects.filter(title=title)
            obj = objects.get(user=player)

            obj.gameState = save_State
            obj.save()

        except Save.DoesNotExist:
            obj = Save()
            obj.title = title
            obj.user = player
            obj.gameState = save_State
            obj.save()

        return HttpResponse("OK")


@csrf_exempt
def load(request):
    if request.is_ajax():

        request_data = request.POST
        title = request_data.get('Title')
        player = request.user.username

        objects = Save.objects.filter(title=title)
        obj = objects.get(user=player)


        return HttpResponse(obj.gameState)




def game(request, pk):

    game = Game.objects.get(id=pk)
    all_saves = Save.objects.all()

    args = {'user': request.user, 'saves': all_saves, 'game': game}
    return render(request, "play.html", args)

def hardcoded(request):

    return render(request, "hardcoded_game.html")
