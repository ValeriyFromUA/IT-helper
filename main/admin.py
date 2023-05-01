from django.contrib import admin

from .models import Customer, Staff, Task

admin.site.register(Customer)
admin.site.register(Task)
admin.site.register(Staff)
