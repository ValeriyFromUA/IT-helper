from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = models.CharField(max_length=200, blank=False, unique=False)
    email = models.EmailField(unique=True, null=False)
    city = models.CharField(blank=False, default='Kyiv')
    street = models.CharField(blank=True)
    house = models.CharField(blank=True)
    apartment = models.CharField(blank=True)
    phone = models.CharField(blank=False)
    is_confirmed = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)


class Confirmations(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    confirmation_key = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)


class Category(models.Model):
    name = models.CharField(null=False)
    description = models.CharField(blank=True)


class Task(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    employee = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    description = models.CharField(max_length=1000, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    finished = models.BooleanField(default=False)
