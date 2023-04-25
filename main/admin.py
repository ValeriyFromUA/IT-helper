from django.contrib import admin

from .models import Category, Customer, Staff, Task

admin.site.register(Customer)
admin.site.register(Task)
admin.site.register(Category)
admin.site.register(Staff)
