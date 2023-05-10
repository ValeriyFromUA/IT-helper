from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from ..models import Price


class PriceView(ListView):
    model = Price
    template_name = "price.html"
    context_object_name = "price"
    ordering = ["category"]
