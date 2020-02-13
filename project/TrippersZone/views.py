from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .serializers import ownerSerializer
from TrippersZone.serializers import ownerSerializer
from .models import renter, owner, OwnerPost
from django import forms
from .forms import NameForm, CreatePost, Search, Oform
from django.contrib.auth import logout as django_logout
from .forms import NameForm, Oform, CreatePost, Search
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import login
import random
from django.contrib.auth import authenticate, login as dj_login


def index(request):
    return render(request, 'index.html')


def post(request):
    return HttpResponse("<h1> this is a test post </h1>")


def signup(request):
    print("signup started")
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            print("till 1")
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')  # !!!! we used password 1 method
            print("till 2")
            user = authenticate(username=username, password=raw_password)
            dj_login(request, user)
            print("till 3")
            return redirect('/TrippersZone/set_profile')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def renter_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)  # sending data to authentication
            dj_login(request, user)
            return redirect('/TrippersZone/set_owner_profile')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def profile(request):
    global renter
    renter = renter.objects.get(Rname=request.user.username)
    return render(request, 'profile.html', {'renter': renter})  # model -> renter -> base -> page


def logout(request):
    django_logout(request)  # logout current user
    return redirect('index')


def owner_profile(request):
    return render(request, 'owner_profile.html')  # after owner login  load this


def create_post(request):
    return render(request, 'create_post.html')  # owner post vacancy page


# storing data from post to database
def createPostProcess(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CreatePost(request.POST)
        # check whether it's valid:
        if form.is_valid():
            OwnerPost.objects.create(Opost=form.cleaned_data['Opost'],
                                     OpostedBy=request.user.username,
                                     OroomRent=form.cleaned_data["OroomRent"],
                                     Olocation=form.cleaned_data["Olocation"])
            return redirect('/TrippersZone/owner_profile')

    # if GET
    else:
        form = CreatePost()
    return render(request, 'create_post.html', {'form': form})


def login(request):
    print("login startes")
    if request.method == 'POST':
        print("till s1")
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            print("form is valid")
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = form.get_user()

            dj_login(request, user)

            return redirect('/TrippersZone/owner_profile')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html')  # if error replace {'form': form})


def renter_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = form.get_user()

            dj_login(request, user)

            return redirect('/TrippersZone/profile')
    else:
        form = AuthenticationForm()
    return render(request, 'renter_login.html')  # if error replace {'form': form})


def o_home(request):
    return render(request, 'o_home.html')


def o_login(request):
    return render(request, 'o_login.html')  # using google login method


def owner_set_profile(request):
    return render(request, 'set_owner_profile.html')  # takes owners room info


def owner_singupprocess(request):
    print("working")
    if request.method == 'POST':
        form = Oform(request.POST)
        print("till done fffrrrrr")
        if form.is_valid():
            print("tilllaaaaaaaaa ok")
            owner.objects.create(Oname=form.cleaned_data['Oname'], Ocontact=form.cleaned_data['Ocontact'],
                                 Olocation=form.cleaned_data['Olocation'], Ogender=form.cleaned_data['Ogender'],
                                 OnumOfRoom=form.cleaned_data['OnumOfRoom'], Ocapacity=form.cleaned_data['Ocapacity'],
                                 OroomRent=form.cleaned_data['OroomRent'], Oid=random.randint(1000, 9999))
            return redirect('index')
        else:
            form = Oform()
        return render(request, 'set_owner_profile.html', {'form': form})


def set_profile(request):
    return render(request, 'set_profile.html')


def singupprocess(request):
    if request.method == 'POST':
        # create a form instance
        form = NameForm(request.POST)
        # check whether it's valid:

        if form.is_valid():
            renter.objects.create(Rname=form.cleaned_data['Rname'], Rlocation1=form.cleaned_data['Rlocation1'],
                                  Rlocation2=form.cleaned_data['Rlocation2'], Rcontact=form.cleaned_data['Rcontact'],
                                  Rgender=form.cleaned_data['Rgender'], RnumOfGuest=form.cleaned_data['RnumOfGuest'],
                                  Rid=random.randint(1000, 9999))

            return redirect('index')

    # if a GET  tahole change korbo pore jate shoja namaite pari
    # adding info to database
    else:
        form = NameForm()

    return render(request, 'set_profile.html', {'form': form})


def owner_signup(request):
    print("owner signup started")
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            print("till 1")
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')  # !!!! we used used password 1 method
            print("till 2")
            user = authenticate(username=username, password=raw_password)
            dj_login(request, user)
            print("till 3")
            return redirect('/TrippersZone/owner_set_profile')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def o_list(request):
    print("hello")
    vt = owner.objects.all()
    return render(request, 'o_list.html', {'owner': vt})


def test1(request, name):
    print("working")
    vt = owner.objects.get(Oname=name)
    return render(request, 'test1.html', {'owner': vt})


def ownerPostList(request):
    post = OwnerPost.objects.all()
    print("till done")
    return render(request, 'ownerPost.html', {'post': post})


def set_owner_profile(request):
    return HttpResponse("<h1> this is set profile </h1>")


# rest api starts here ------

class ownerlist(APIView):
    # transfring data to GET data
    def get(self, request):
        owners = owner.objects.all()
        serializer = ownerSerializer(owner, many=True)
        return Response(serializer.data)

    # recive data
    def post(self, request):
        owners = owner.objects.all()
        serializer = ownerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)


# logout current user
def logout(request):
    django_logout(request)
    return redirect('index')


class renterlist(APIView):
    # transfring data to GET data
    def get(self, request):
        renters = renter.objects.all()
        serializer = ownerSerializer(owner, many=True)
        return Response(serializer.data)

    # recive data
    def post(self, request):
        renters = renter.objects.all()
        serializer = ownerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
