from django import forms
from django.forms import modelformset_factory

from djcar.core.models import Car


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = "__all__"


CarFormSet = modelformset_factory(Car, extra=0, exclude=())
