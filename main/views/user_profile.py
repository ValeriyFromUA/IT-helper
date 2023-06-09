from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView

from ..models import Customer, Task


class UserProfileView(LoginRequiredMixin, DetailView):
    model = Customer
    template_name = "profile.html"
    context_object_name = "customer"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tasks = Task.objects.filter(client=self.object.id).order_by("-created")
        context["tasks"] = tasks
        return context
