from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views import View
from ..models import Task


class DeleteTaskView(LoginRequiredMixin, View):
    @staticmethod
    def post(request, pk):
        task = get_object_or_404(Task, id=pk)
        if request.customer.is_staff:
            task.delete()
        return redirect(reverse("staff_main"))
