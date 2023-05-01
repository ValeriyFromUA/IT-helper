from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View


class StaffLoginView(View):
    @staticmethod
    def get(request):
        return render(request, "staff_login.html")

    @staticmethod
    def post(request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is None:
            messages.error(request, "Username OR password does not exist")
            return render(request, "login.html")

        if user.is_staff:
            login(request, user)
            return redirect(reverse("staff_main"))

        login(request, user)
        return redirect(reverse("profile", args=[user.id]))
