# Important
from django.shortcuts import render 

# Create your views here.

# account/views.py

from django.shortcuts import render, redirect
from .forms import MyUserCreationForm

def register(request):
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page after registration
    else:
        form = MyUserCreationForm()
    return render(request, 'account/register.html', {'form': form})

from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
    return render(request, 'account/profile.html')