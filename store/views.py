from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index.html', {'context': 'context'})


def login(request):
    return render(request, 'login.html', {'context': 'context'})
