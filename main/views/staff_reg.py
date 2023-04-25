from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.views import View

from ..forms import NewStaffForm


class StaffRegistrationView(View):
    @staticmethod
    def get(request):
        form = NewStaffForm()
        return render(request, "staff_registration.html", {"form": form})

    @staticmethod
    def post(request):
        form = NewStaffForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            login(request, user)
            return redirect("confirm")
        else:
            if "email" in form.errors:
                messages.error(request, "Invalid email address")
            if "username" in form.errors:
                messages.error(request, "Invalid username")
            if "password1" in form.errors:
                messages.error(request, "Invalid password")
            if "password2" in form.errors:
                messages.error(request, "Passwords do not match")

        return render(request, "register.html", {"form": form})

    def form_valid(self, form):
        user = form.save(commit=False)
        user.save()
        login(self.request, user)
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "An error occurred during registration")
        return super().form_invalid(form)
