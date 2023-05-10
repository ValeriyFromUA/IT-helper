from django.shortcuts import render
from django.views.generic import ListView
from ..models import Feedback


class HomeView(ListView):
    template_name = "home.html"
    model = Feedback
    context_object_name = "comments"
    queryset = Feedback.objects.order_by("-id")[:3]
