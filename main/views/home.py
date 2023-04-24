from django.shortcuts import render
from django.views import View


class HomeView(View):
    @staticmethod
    def get(request):
        template_name = "home.html"
        return render(request, template_name)
