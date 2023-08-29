from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = models.CharField(db_index=True, max_length=100, editable=True, unique=True)
    is_verified = models.BooleanField(default=False)
    email = models.EmailField(db_index=True, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
