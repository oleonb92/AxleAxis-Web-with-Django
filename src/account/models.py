# important
from django.db import models 

# Create your models here.

# account/models.py

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class MyUserManager(BaseUserManager):
    # A manager for the custom user model

    def create_user(self, email, password=None):
        # Creates and saves a user with the given email and password
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        # Creates and saves a superuser with the given email and password
        user = self.create_user(email, password=password)
        user.is_admin = True
        user.save(using=self._db)
        return user

class MyUser(AbstractBaseUser):
    # Custom user class implementing AbstractBaseUser
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        # User has a specific permission?
        return True

    def has_module_perms(self, app_label):
        # User has permissions to view the app `app_label`?
        return True

    @property
    def is_staff(self):
        # Is the user a member of staff?
        return self.is_admin
