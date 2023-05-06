from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views import View
from django.forms import formset_factory
from ..forms import PriceForm
from ..models import Price


class NewPriceView(View):
    PriceSet = formset_factory(PriceForm, extra=5)
    price_set = PriceSet()

    def get(self, request):
        return render(request, "new_price.html", {"price_set": self.price_set})

    def post(self, request):
        set = self.PriceSet(request.POST)
        if not set.is_valid():
            messages.error(request, "Щось пішло не так")
        else:
            for price in set:
                data = price.cleaned_data
                service = Price(category=data.get("category"), description=data.get("description"),
                                price=data.get("price"))
                if data.get("category") is not None:
                    service.save()
            return redirect(reverse("price"))

        return render(request, "new_price.html", {"price_set": self.price_set})
