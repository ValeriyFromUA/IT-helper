from django.contrib.auth.models import AbstractUser
from django.db import models


class Customer(AbstractUser):
    city = models.CharField(max_length=200, null=True, default='Kyiv')
    street = models.CharField(max_length=200, null=True)
    house = models.CharField(max_length=200, null=True)
    apartment = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=False)
    is_confirmed = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)


class Confirmations(models.Model):
    user_ref = models.ForeignKey(Customer, on_delete=models.CASCADE)
    confirmation_key = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)


class Category(models.Model):
    name = models.CharField(max_length=200, null=False)
    description = models.CharField(max_length=1000, null=True)


class Task(models.Model):
    client = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='task_client')
    city = models.CharField(max_length=200, null=True, default='Kyiv')
    street = models.CharField(max_length=200, null=True)
    house = models.CharField(max_length=200, null=True)
    apartment = models.CharField(max_length=200, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    description = models.CharField(max_length=1000, null=False)
    created = models.DateTimeField(auto_now_add=True)
    in_work = models.BooleanField(default=False)
    finished = models.BooleanField(default=False)
    employee = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, related_name='task_employee')
