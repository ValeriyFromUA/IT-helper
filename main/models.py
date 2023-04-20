from django.contrib.auth.models import User
from django.db import models


class Customer(User):
    city = models.CharField(max_length=200, blank=False, default='Kyiv')
    street = models.CharField(max_length=200, blank=True)
    house = models.CharField(max_length=200, blank=True)
    apartment = models.CharField(max_length=200, blank=True)
    phone = models.CharField(max_length=200, blank=False)
    is_confirmed = models.BooleanField(default=False)


class Staff(User):
    city = models.CharField(max_length=200, blank=False, default='Kyiv')
    street = models.CharField(max_length=200, blank=True)
    house = models.CharField(max_length=200, blank=True)
    apartment = models.CharField(max_length=200, blank=True)
    phone = models.CharField(max_length=200, blank=False)


class Confirmations(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    confirmation_key = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)


class Category(models.Model):
    name = models.CharField(max_length=200, null=False)
    description = models.CharField(max_length=1000, blank=True)


class Task(models.Model):
    client = models.ForeignKey(Customer, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    description = models.CharField(max_length=1000, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    in_work = models.BooleanField(default=False)
    finished = models.BooleanField(default=False)
    employee = models.ForeignKey(Staff, on_delete=models.CASCADE, null=True, blank=True)
