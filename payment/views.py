import urllib.parse
import urllib.request
import uuid
from hashlib import md5

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.db.models import Sum
from django.shortcuts import render, redirect

from gamestore.settings import seller_id, seller_key
from payment.models import Transaction
from store.models import Game


def generate_checksum(list):
    str = urllib.parse.urlencode(list)
    md = md5(str.encode("ascii"))
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

    context = {'pid': pid, 'sid': seller_id, 'amount': amount, 'checksum': checksum, 'username': username,
               'game': game.title}

    return render(request, 'payment/payment_checkout.html', context)


@login_required
def verification_view(request):
    pid = request.GET.get('pid')
    ref = request.GET.get('ref')
    result = request.GET.get('result')
    checksum = request.GET.get('checksum')
    local = generate_checksum({'pid': pid, 'ref': ref, 'result': result, 'token': seller_key})

    if checksum == local:
        obj = Transaction.objects.get(pid=pid)
        if result == 'success':
            obj.state = 'SUCCESS'
            obj.save()
        elif result == 'cancel':
            obj.state = 'CANCEL'
            obj.save()
        else:
            obj.state = 'ERROR'
            obj.save()
    return redirect('game_detail', pk=obj.game.pk)


@login_required
def detail_view(request, uuid):
    username = request.user.username
    user = User.objects.get(username=username)

    transaction = Transaction.objects.get(pid=uuid)

    if transaction.user == user:
        return render(request, 'payment/payment_detail.html', {'transaction': transaction})
    return redirect('payment_list')


@login_required
def list_view(request):
    username = request.user.username
    user = User.objects.get(username=username)
    transaction_list = Transaction.objects.filter(user=user)
    reversed_transactions = list(reversed(transaction_list))
    paginator = Paginator(reversed_transactions, 25)

    page = request.GET.get('page', 1)
    transactions = paginator.get_page(page)

    return render(request, 'payment/payment_list.html', {'transactions': transactions})


@login_required
def sales_view(request, pk):
    game = Game.objects.get(pk=pk)
    username = request.user.username
    user = User.objects.get(username=username)
    if game.game_owner == user:
        transaction_list = Transaction.objects.filter(game=game).filter(state='SUCCESS')
        reversed_transactions = list(reversed(transaction_list))
        paginator = Paginator(reversed_transactions, 25)

        page = request.GET.get('page', 1)
        transactions = paginator.get_page(page)

        total = list(transaction_list.aggregate(total_price=Sum('amount')).values())[0]

        return render(request, 'payment/payment_sales.html',
                      {'game': game, 'transactions': transactions, 'total': total})
    else:
        return redirect('index')

# Pagination
# https://docs.djangoproject.com/en/2.1/topics/pagination/
