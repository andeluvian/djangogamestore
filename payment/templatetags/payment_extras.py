from django import template
from payment.models import Transaction


register = template.Library()
##locale.setlocale(locale.LC_ALL, 'fi_FI.UTF-8')
@register.filter(name='price')
def price(value):
    return locale.currency(value, grouping=True)



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
    return Transaction.objects.filter(user=user).filter(game=game).filter(state='SUCCESS').exists()
