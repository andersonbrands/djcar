from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic import FormView

from djcar.core.forms import CarForm, CarFormSet


# Create your views here.
class Home(View):
    formset_class = CarFormSet
    template_name = "core/index.html"

    def get(self, request):
        context = {"formset": self.formset_class()}
        return render(request, self.template_name, context)

    def post(self, request):
        formset = self.formset_class(request.POST)
        if formset.is_valid():
            formset.save()
            return HttpResponseRedirect(".")

        return render(request, self.template_name, {"formset": formset})


class AddCarView(FormView):
    form_class = CarForm
    template_name = "core/add_car.html"
    success_url = "."

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Success")
        return super().form_valid(form)
