from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from ..forms import TaskForm


class NewTaskView(View):
    @staticmethod
    def get(request):
        return render(request, "new_post.html")

    @staticmethod
    def post(request):
        task_form = TaskForm(request.POST)
        if task_form.is_valid():
            task = task_form.save(commit=False)
            task.client = request.user

        return redirect(reverse("profile", args=[request.user.id]))
