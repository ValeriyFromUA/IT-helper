from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views import View

from ..forms import UserDataForm
from ..models import Customer


class EditProfileView(LoginRequiredMixin, View):
    @staticmethod
    def get(request, pk):
        customer = get_object_or_404(Customer, id=pk)
        form = UserDataForm(instance=customer)
        return render(request, "edit_profile.html", {"form": form})

    @staticmethod
    def post(request, pk):
        customer = get_object_or_404(Customer, id=pk)
        form = UserDataForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            customer.city = form.cleaned_data["city"]
            customer.street = form.cleaned_data["street"]
            customer.house = form.cleaned_data["house"]
            customer.apartment = form.cleaned_data["apartment"]
            customer.user_name = form.cleaned_data["user_name"]
            customer.save()
            return redirect(reverse("profile", args=[pk]))
        return render(request, "edit_profile.html", {"form": form})
