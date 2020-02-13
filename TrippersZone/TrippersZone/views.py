from django.shortcuts import render
from django.http import HttpResponse
from .models import renter
from .models import owner
from .models import OwnerPost
from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth import logout as django_logout
from .forms import NameForm, Oform, CreatePost, Search


# Create your views here.


def index(request):
    return render(request, "index.html")


def post(request):
    return HttpResponse("<h1>This is post</h1>")


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')

            login(request, user)

            return redirect('/TrippersZone/profile')  # redirecting to profile page
        else:
            form = AuthenticationForm()
        return render(request, 'login.html')  # if error replace {'form': form})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')  # !!!! we used used password 1 method
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/TrippersZone/set_profile')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def owner_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)  # sending data to authentication
            login(request, user)
            return redirect('/TrippersZone/set_owner_profile')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def owner_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = form.get_user()

            login(request, user)

            return redirect('/TrippersZone/student_profile')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html')  # if error replace {'form': form})


def profile(request):
    global renter
    teacher = renter.objects.get(Tname=request.user.username)
    return render(request, 'profile.html', {'renter': renter})  # model -> renter -> base -> page
