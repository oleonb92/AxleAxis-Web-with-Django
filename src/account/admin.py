# Important
from django.contrib import admin

# Register your models here.

# account/admin.py

from django.contrib import admin
from .models import MyUser

admin.site.register(MyUser)
