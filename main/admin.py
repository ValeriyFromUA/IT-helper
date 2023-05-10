from django.contrib import admin

from .models import Customer, Staff, Task, Category, Price, Feedback

admin.site.register(Customer)
admin.site.register(Task)
admin.site.register(Staff)
admin.site.register(Category)
admin.site.register(Price)
admin.site.register(Feedback)
