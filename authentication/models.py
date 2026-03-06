from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ADMIN = 'admin'
    USER = 'user'
    
    ROLE_CHOICES = (
        (ADMIN, 'admin'),
        (USER, 'user'),
    )
    
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default=USER)
