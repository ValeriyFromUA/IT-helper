from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views import View

from ..forms import FullTaskForm
from ..models import Task


class StaffTaskView(LoginRequiredMixin, View):
    def get(self, request, pk):
        task = get_object_or_404(Task, id=pk)
        form = FullTaskForm(instance=task)
        return render(request, "staff_task.html", context={"form": form})

    def post(self, request, pk):
        task = get_object_or_404(Task, id=pk)
        form = FullTaskForm(request.POST, request.FILES, instance=task)
        finished = bool(request.POST.get("finished"))
        in_work = bool(request.POST.get("in_work"))

        if not form.is_valid():

            messages.error(request, "Невірно введені данні")
        else:
            task.phone = form.cleaned_data["phone"]
            task.city = form.cleaned_data["city"]
            task.street = form.cleaned_data["street"]
            task.house = form.cleaned_data["house"]
            task.apartment = form.cleaned_data["apartment"]
            task.description = form.cleaned_data["description"]
            task.price = form.cleaned_data["price"]
            task.finished = finished
            if finished:
                task.in_work = True
            else:
                task.in_work = in_work
            task.save()
            return redirect(reverse("staff_main"))

        return render(request, "staff_task.html", {"form": form})
