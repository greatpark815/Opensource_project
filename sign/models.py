from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    user_level = models.CharField(max_length =20, default='')
    email=models.EmailField(verbose_name = "email", max_length = 255, unique = True)
    