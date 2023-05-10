from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views import View

from ..forms import TaskForm
from ..models import Customer
from ..telegram_bot import send_telegram_message, make_text_for_sending


class NewTaskView(View):
    @staticmethod
    def get(request):
        customer = get_object_or_404(Customer, id=request.user.id)
        return render(request, "new_task.html", {"customer": customer})

    @staticmethod
    def post(request):
        form = TaskForm(request.POST)
        if not form.is_valid():
            messages.error(request, "Щось пішло не так")
        else:
            task = form.save(commit=False)
            task.client = request.user
            task.save()
            send_telegram_message(
                make_text_for_sending(task.created, task.client.user_name, task.phone, task.city, task.street,
                                      task.house,
                                      task.apartment, task.description))
            return redirect(reverse("profile", args=[request.user.id]))

        return render(request, "new_task.html", {"form": form})
