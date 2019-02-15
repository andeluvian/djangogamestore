from functools import wraps
from django.core.exceptions import PermissionDenied


def ajax_required(view):
    @wraps(view)
    def _wrapped_view(request, *args, **kwargs):
        if request.is_ajax():
            return view(request, *args, **kwargs)
        else:
            raise PermissionDenied()
    return _wrapped_view


# Require ajax decorator
# https://stackoverflow.com/questions/34152909/django-custom-decorator-to-allow-only-ajax-request#34171567
