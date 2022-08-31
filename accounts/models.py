from django.db import models
from django.contrib.auth.models import AbstractUser


class Account(AbstractUser):
    username = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    is_seller = models.BooleanField()

    REQUIRED_FIELDS = ["first_name", "last_name"]
