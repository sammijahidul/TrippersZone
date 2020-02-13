from __future__ import unicode_literals

from django.contrib import admin
# Register your models here.
from .models import renter, owner, OwnerPost

admin.site.register(renter)
admin.site.register(owner)
admin.site.register(OwnerPost)