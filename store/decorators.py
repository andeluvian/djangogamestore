from functools import wraps
from django.core.exceptions import PermissionDenied
from .models import Game


def ajax_required(view):
    @wraps(view)
    def _wrapped_view(request, *args, **kwargs):
        if request.is_ajax():
            return view(request, *args, **kwargs)
        else:
            raise PermissionDenied()
    return _wrapped_view


def game_required(view):
    @wraps(view)
    def _wrapper_view(request, *args, **kwargs):
        game = Game.objects.get(pk=kwargs['pk'])
        if request.user.transaction_set.filter(game=game).filter(state='SUCCESS').exists():
            return view(request, *args, **kwargs)
        else:
            raise PermissionDenied()
    return _wrapper_view


# Require ajax decorator
# https://stackoverflow.com/questions/34152909/django-custom-decorator-to-allow-only-ajax-request#34171567
