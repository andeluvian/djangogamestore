import uuid
import urllib.request
import urllib.parse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
from hashlib import md5
from .models import Transaction
from django.contrib.auth.models import User
from store.models import Game


# TODO: replace with environmental variables
seller_id = 'SmallGameStore'
seller_key = '19467677922774a4b3de618c3f86177f'


def generate_checksum(list):
    list_str = urllib.parse.urlencode(list)
    md = md5(list_str.encode("ascii"))
    checksum = md.hexdigest()
    return checksum


@login_required
def checkout_view(request, pk):
    game = Game.objects.get(pk=pk)
    amount = game.price
    username = request.user.username
    user = User.objects.get(username=username)

    transactions = Transaction.objects.filter(user=user).filter(game=game)

    # if game is already paid for
    if transactions.filter(state='SUCCESS').exists():
        return redirect('game_detail', pk=pk)

    # if a transaction exists but still needs to be paid, else create a new transaction
    pending_transaction = transactions.filter(state='PENDING')
    if pending_transaction.exists():
        obj = pending_transaction.first()
        pid = obj.pid
        checksum = generate_checksum({'pid': pid, 'sid': seller_id, 'amount': amount, 'token': seller_key})
    else:
        pid = uuid.uuid4()
        checksum = generate_checksum({'pid': pid, 'sid': seller_id, 'amount': amount, 'token': seller_key})
        obj = Transaction(pid=pid, amount=amount, user=user, game=game)
        obj.save()

    context = {'pid': pid,'sid': seller_id,'amount': amount,'checksum': checksum, 'username': username, 'game': game.title }

    return render(request, 'payment/payment_checkout.html', context)


@login_required
def processing_view(request):
    # TODO: redirect to game page

    pid = request.GET.get('pid')
    ref = request.GET.get('ref')
    result = request.GET.get('result')
    checksum = request.GET.get('checksum')
    local_checksum = generate_checksum({'pid': pid, 'ref': ref, 'result': result, 'token': seller_key})

    obj = Transaction.objects.get(pid=pid)
    if checksum == local_checksum:
        if result == 'success':
            obj.state = 'SUCCESS'
            obj.save()
        elif result == 'cancel':
            obj.state = 'CANCEL'
            obj.save()
        else:
            obj.state = 'ERROR'
            obj.save()
    return redirect('index')


def detail_view(request, uuid):
    transaction = Transaction.objects.get(pid=uuid)

    return render(request, 'payment/payment_detail.html', { 'transaction': transaction })


def list_view(request):
    transaction_list = Transaction.objects.all()
    reversed_transactions = list(reversed(transaction_list))
    paginator = Paginator(reversed_transactions, 25)

    page = request.GET.get('page', 1)
    transactions = paginator.get_page(page)

    return render(request, 'payment/payment_list.html', { 'transactions': transactions })


# TODO: list transactions for user
# TODO: list transactions for game


# Pagination
# https://docs.djangoproject.com/en/2.1/topics/pagination/