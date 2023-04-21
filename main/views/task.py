from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View

from ..models import Task


class TaskView(LoginRequiredMixin, View):
    def get(self, request, pk):
        task = get_object_or_404(Task, id=pk)
        return render(request, "task.html", context={"task": task})

    def post(self, request, pk):
        task = get_object_or_404(Task, id=pk)
        finished = bool(request.POST.get("finished"))
        in_work = bool(request.POST.get("in_work"))
        if in_work:
            task.employee = request.user
        if not in_work:
            task.employee = None
        task.finished = finished
        task.in_work = in_work
        task.save()

        return redirect("task", pk=pk)
