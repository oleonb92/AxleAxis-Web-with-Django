# Important
from django.shortcuts import render

# Create your views here.

# Example in personal/views.py

from django.shortcuts import render

def home(request):
    return render(request, 'personal/home.html')
