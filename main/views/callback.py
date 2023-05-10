from django.shortcuts import redirect, render
from django.views import View

from ..formatter import format_phone
from ..forms import CallBackForm
from ..telegram_bot import send_telegram_message


class CallBackView(View):
    @staticmethod
    def get(request):
        return render(request, "callback.html")

    @staticmethod
    def post(request):
        form = CallBackForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.phone = format_phone(data.phone)
            data.save()
            send_telegram_message(
                f"{data.name} просить зв'язатися з ним за номером {data.phone}")
            return redirect("home")
