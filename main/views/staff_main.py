from django.views.generic import ListView

from ..models import Task


class StaffMainView(ListView):
    template_name = "staff_main.html"
    model = Task
    context_object_name = "tasks"
    ordering = ["-id"]
