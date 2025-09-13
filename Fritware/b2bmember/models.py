from django.db import models
from django.contrib.auth.models import AbstractUser
import random


class memberSignup(models.Model):
    user = models.CharField(max_length=100)
    name = models.CharField(max_length=60)
    email = models.EmailField(max_length=80)
    password = models.CharField()
    
