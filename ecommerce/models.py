from django.db import models
from django.contrib.auth.models import AbstractUser


class UserType(models.TextChoices):
    BUYER = 'buyer', 'Buyer'
    SELLER = 'seller', 'Seller'


class CustomUser(AbstractUser):
    user_type = models.CharField(max_length=10, choices=UserType.choices)

    def __str__(self):
        return str(self.username)
