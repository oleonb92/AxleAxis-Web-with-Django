"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# Important
# from django.contrib import admin
# from django.urls import path

# urlpatterns = [
#     path("admin/", admin.site.urls),
# ]

# mysite/urls.py

from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views  # Import for the login and logout views
from account.views import register  # Import the register view
from personal.views import home  # Import the home view
from account.views import profile  # Import the profile view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # Homepage URL
    path('register/', register, name='register'),  # Registration URL
    path('login/', auth_views.LoginView.as_view(template_name='account/login.html'), name='login'),  # Login URL
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),  # Logout URL
    path('profile/', profile, name='profile'),  # Add this line for the profile page
    # You can add other URL patterns here as needed
]

