from django.contrib import admin
from .models import User, Staff, Task, Category

admin.site.register(User)
admin.site.register(Staff)
admin.site.register(Task)
admin.site.register(Category)
