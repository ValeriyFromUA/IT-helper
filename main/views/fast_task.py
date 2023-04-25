from django.shortcuts import render, redirect
from django.views import View
from ..forms import FastTaskForm
from django.contrib import messages


class FastTaskView(View):
    @staticmethod
    def get(request):
        return render(request, "fast_task.html")

    @staticmethod
    def post(request):
        form = FastTaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.save()
            return redirect("home")
