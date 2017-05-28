from django.shortcuts import render, redirect
from .forms import ClientCreateForm, PeddlerCreateForm, EstablishedCreateForm, ClientUpdateForm, EstablishedUpdateForm, \
    PeddlerUpdateForm
from .models import Peddler, Established, Client
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user

def delete_user(request):
    passw = request.POST.get('passw')
    if request.method == 'POST':
        username = get_user(request)
        user = authenticate(request, username=username, password=passw)
        if user is not None:
            u = request.user
            u.delete()
            return redirect('map:index')
    return render(request, 'delete.html', {'passw':passw})


@login_required(login_url='/account/login')
def edit_user(request):
    if Peddler.objects.filter(user=request.user).exists():
        return redirect('account:edit_peddler')
    elif Client.objects.filter(user=request.user).exists():
        return redirect('account:edit_client')
    else:
        return redirect('account:edit_established')

@login_required(login_url='/account/login')
def edit_client(request):
    try:
        profile = request.user
    except Client.DoesNotExist:
        profile = Client(user=request.user)
    if request.method == 'POST':
        form = ClientUpdateForm(data=request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('map:index')
    else:
        form = ClientUpdateForm(instance=request.user)
    return render(request, 'edit_client.html', {'form': form})

@login_required(login_url='/account/login')
def edit_peddler(request):
    try:
        profile = request.user
    except Peddler.DoesNotExist:
        profile = Peddler(user=request.user)
    if request.method == 'POST':
        form = PeddlerUpdateForm(data=request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('map:index')
    else:
        form = PeddlerUpdateForm(instance=request.user)
    return render(request, 'edit_peddler.html', {'form': form})

@login_required(login_url='/account/login')
def edit_established(request):
    try:
        profile = request.user
    except Established.DoesNotExist:
        profile = Established(user=request.user)
    if request.method == 'POST':
        form = EstablishedUpdateForm(data=request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('map:index')
    else:
        form = EstablishedUpdateForm(instance=request.user)
    return render(request, 'edit_established.html', {'form': form})


def new_item(request):
    context = {}
    return render(request, 'item_new.html', context)


def register(request):
    return render(request, 'register_base.html')


def register_client(request):
    if request.method == 'POST':
        form = ClientCreateForm(request.POST)
        if form.is_valid():
            user, user_profile = form.save()
            user.save()
            user = authenticate(username=user.username, password=user.password)
            if user is not None:
                login(request, user)
                return redirect('map:index')
    else:
        form = ClientCreateForm()
    return render(request, 'register_client.html', {'form': form})


def register_peddler(request):
    if request.method == 'POST':
        form = PeddlerCreateForm(request.POST)
        if form.is_valid():
            user, user_profile = form.save()
            user.save()
            user = authenticate(username=user.username, password=user.password)
            if user is not None:
                login(request, user)
                return redirect('map:index')
    else:
        form = PeddlerCreateForm()
    return render(request, 'register_peddler.html', {'form': form})


def register_established(request):
    if request.method == 'POST':
        form = EstablishedCreateForm(request.POST)
        if form.is_valid():
            user, user_profile = form.save()
            user.save()
            user = authenticate(username=user.username, password=user.password)
            login(request, user)
            return redirect('map:index')
    else:
        form = EstablishedCreateForm()
    return render(request, 'register_established.html', {'form': form})
