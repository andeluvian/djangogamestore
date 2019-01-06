from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Game

# Create your views here.
def index(request):
    user_count = User.objects.count()  # Only to verify the registration form works, delete later
    return render(request, 'index.html', {'user_count': user_count})


def login(request):
    return render(request, 'login.html', {'context': 'context'})

def register(request):
    return render(request, 'register.html', {'context': 'context'})

def gamelist(request):
    template_name = "gamelist.html"
    queryset = Game.objects.all()
    context = {
        "name" : "kena",
        "object_list": queryset
    }
    return render(request, template_name, context)



class GameList(ListView):
    queryset = Game.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        return context

#class GameDetail(DetailView):
#    model = Game
