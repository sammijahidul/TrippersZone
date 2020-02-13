from __future__ import unicode_literals
from django.db import models

from django.db import models
from django.utils import timezone


# Create your models here.
class renter(models.Model):
    Rid = models.CharField(max_length=225)
    Rname = models.CharField(max_length=255)
    Rcontact = models.CharField(max_length=255)
    Rlocation1 = models.CharField(max_length=255)
    Rlocation2 = models.CharField(max_length=255)
    Rgender = models.CharField(max_length=255)
    RnumOfGuest = models.CharField(max_length=255)

    """docstring for ClassName"""

    def __str__(self):
        return self.Rname


class owner(models.Model):
    Oid = models.CharField(max_length=225)
    Oname = models.CharField(max_length=255)
    Ocontact = models.CharField(max_length=255)
    Olocation = models.CharField(max_length=255)
    Ogender = models.CharField(max_length=255)
    OnumOfRoom = models.CharField(max_length=255)
    Ocapacity = models.CharField(max_length=255)
    OroomRent = models.CharField(max_length=255)

    """docstring for ClassName"""

    def __str__(self):
        return self.Oname


class OwnerPost(models.Model):
    Opost = models.CharField(max_length=300)
    OpostedBy = models.CharField(max_length=225)
    OpostTime = models.DateField(default=timezone.now)
    OnumOfRoom = models.CharField(max_length=10)
    OroomRent = models.CharField(max_length=225)
    Olocation = models.CharField(max_length=225)

    def __str__(self):
        return self.OpostedBy

    def __str__(self):
        return self.Opost[:150]
