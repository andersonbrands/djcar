from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import FormView

from djcar.core.forms import CarForm, CarFormSet


# Create your views here.
class Home(View):
    formset_class = CarFormSet

    def get(self, request):
        context = {"formset": self.formset_class()}
        return render(request, "core/index.html", context)


class AddCarView(FormView):
    form_class = CarForm
    template_name = "core/add_car.html"
    success_url = "."

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Success")
        return super().form_valid(form)
