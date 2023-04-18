from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View


class LogoutView(LoginRequiredMixin, View):
    @staticmethod
    def get(request):
        logout(request)
        return redirect(reverse_lazy("login"))
