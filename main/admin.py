from django.contrib import admin
from .models import Customer, Task, Category, Staff

admin.site.register(Customer)
admin.site.register(Staff)
admin.site.register(Task)
admin.site.register(Category)
