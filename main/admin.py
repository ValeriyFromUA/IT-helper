from django.contrib import admin

from .models import Category, Customer, Task, Staff

admin.site.register(Customer)
admin.site.register(Task)
admin.site.register(Category)
admin.site.register(Staff)
