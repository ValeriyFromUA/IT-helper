from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View

from ..forms import FeedbackForm


class FeedbackView(View):
    @staticmethod
    def get(request):
        return render(request, "feedback.html")

    @staticmethod
    def post(request):
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.client = request.user
            feedback.save()

            return redirect("home")
        return HttpResponse("Помилка. Щось пішло не так")
