from django.shortcuts import render


# Create your views here.

def index(request):
    context = {}
    return render(request, 'login.html', context)


def login(request):
    context = {}
    return render(request, 'login.html', context)


def register(request):
    context = {}
    return render(request, 'register.html', context)
