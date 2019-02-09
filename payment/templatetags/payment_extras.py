import locale
from django import template


register = template.Library()
##locale.setlocale(locale.LC_ALL, 'fi_FI.UTF-8')
@register.filter(name='price')
def price(value):
    return locale.currency(value, grouping=True)
