from random import randrange

from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.views import View

from ..forms import NewUserForm
from ..mail_confirmation import send_confirmation_email
from ..models import Confirmations


class RegistrationView(View):
    @staticmethod
    def get(request):
        form = NewUserForm()
        return render(request, "register.html", {"form": form})

    @staticmethod
    def post(request):
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            login(request, user)
            key = randrange(10000, 99999)
            confirmation = Confirmations(user_id=user, confirmation_key=key)
            confirmation.save()
            send_confirmation_email(user.email, key)
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
        key = randrange(10000, 99999)
        confirmation = Confirmations(user_id=user, confirmation_key=key)
        confirmation.save()
        send_confirmation_email(user.email, key)
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "An error occurred during registration")
        return super().form_invalid(form)
