from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views import View

from ..forms import ConfirmationForm
from ..models import Confirmations, Customer


class ConfirmStaffView(View):
    def get(self, request):
        return render(request, "confirmation_staff.html")
