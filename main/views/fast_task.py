from django.shortcuts import redirect, render
from django.views import View

from ..forms import FastTaskForm
from ..telegram_bot import send_telegram_message, make_text_for_sending


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
            send_telegram_message(
                make_text_for_sending(task.created, task.anonim_user, task.phone, task.city, task.street, task.house,
                                      task.apartment, task.description))
            return redirect("home")
