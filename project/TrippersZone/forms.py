from django import forms
from .models import *
from django.db import models


class NameForm(forms.Form):
    Rname = forms.CharField(label='Rname', max_length=255)
    Rcontact = forms.CharField(label='Rcontact', max_length=255)
    Rlocation1 = forms.CharField(label='Rlocation1', max_length=255)
    Rlocation2 = forms.CharField(label='Rlocation2', max_length=255)
    Rgender = forms.CharField(label='Rgender', max_length=255)
    RnumOfGuest = forms.CharField(label='RnumOfGuest', max_length=255)


class Oform(forms.ModelForm):
    Oname = forms.CharField(label='Oname', max_length=255)
    Ocontact = forms.CharField(label='Ocontact', max_length=255)
    Olocation = forms.CharField(label='Olocation', max_length=255)
    Ogender = forms.CharField(label='Ogender', max_length=255)
    OnumOfRoom = forms.CharField(label='OnumOfRoom', max_length=255)
    Ocapacity = forms.CharField(label='Ocapacity', max_length=255)
    OroomRent = forms.CharField(label='OroomRent', max_length=255)

    class Meta:
        model = owner
        fields = ['Oname', ]


class Search(forms.Form):
    Rname = forms.CharField(label='Rname', max_length=255)


class CreatePost(forms.ModelForm):
    Opost = forms.CharField(widget=forms.TextInput(), label='Opost', max_length=300)

    OroomRent = forms.CharField(widget=forms.TextInput(), label='OroomRent', max_length=255)
    Olocation = forms.CharField(widget=forms.TextInput(), label='Olocation', max_length=255)


    class Meta():
        model = OwnerPost
        fields = ['Opost', 'OroomRent', 'Olocation']
