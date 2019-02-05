from django import template
from payment.models import Transaction


register = template.Library()


@register.filter(name='price')
def price(value):
    if value is None:
        s = ''
    else:
        s = '%.2f€' % value
        s = s.replace('.', ',')
    return s


@register.filter(name='has_game')
def has_game(user, game):
    return Transaction.objects.filter(user=user).filter(game=game).exists()