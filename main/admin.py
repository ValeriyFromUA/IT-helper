from django.contrib import admin

from .models import Category, Customer, Task

admin.site.register(Customer)
admin.site.register(Task)
admin.site.register(Category)
