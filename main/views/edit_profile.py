from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views import View

from ..forms import UserDataForm
from ..models import User


class EditProfileView(LoginRequiredMixin, View):
    @staticmethod
    def get(request, pk):
        user = get_object_or_404(User, id=pk)
        form = UserDataForm(instance=user)
        return render(request, "edit_profile.html", {"form": form})

    @staticmethod
    def post(request, pk):
        user = get_object_or_404(User, id=pk)
        form = UserDataForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            user.city = form.cleaned_data["city"]
            user.street = form.cleaned_data["street"]
            user.house = form.cleaned_data["house"]
            user.apartment = form.cleaned_data["apartment"]
            user.phone = form.cleaned_data["phone"]
            user.save()
            return redirect(reverse("profile", args=[pk]))
        return render(request, "edit_profile.html", {"form": form})
