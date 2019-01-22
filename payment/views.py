import uuid
import urllib.request
import urllib.parse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
from hashlib import md5
from .models import Transaction


# TODO: replace with environmental variables
seller_id = 'SmallGameStore'
seller_key = '19467677922774a4b3de618c3f86177f'


def generate_checksum(list):
    list_str = urllib.parse.urlencode(list)
    md = md5(list_str.encode("ascii"))
    checksum = md.hexdigest()
    return checksum


def payment_view(request):
    # TODO: integrate with game model to fetch reliable price information
    # TODO: limit access to logged in users
    # TODO: if user has an existing pending transaction, use that instead of creating a new one

    # game_id = request.GET.get('id')
    # game = Game.objects.get(id=id)

    pid = uuid.uuid4()
    amount = 5.00
    checksum = generate_checksum({'pid': pid, 'sid': seller_id, 'amount': amount, 'token': seller_key})

    obj = Transaction(pid=pid, amount=amount)
    obj.save()

    context = {'pid': pid,'sid': seller_id,'amount': amount,'checksum': checksum}

    return render(request, 'payment/payment.html', context)


def processing_view(request):
    # TODO: change status to SUCCESS if valid
    # TODO: grant access to game if valid
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


# Pagination
# https://docs.djangoproject.com/en/2.1/topics/pagination/