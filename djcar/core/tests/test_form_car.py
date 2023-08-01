import logging

import pytest

from djcar.core.forms import CarForm
from djcar.core.models import Car


@pytest.fixture
def valid_form():
    data = {
        "model": "Golf",
        "brand": "ford",
        "main_color": "red",
        "value": 50000,
        "production_cost": 10000,
        "transportation_cost": 5000,
    }
    form = CarForm(data)
    assert form.is_valid()

    yield form


@pytest.mark.parametrize(
    "expected",
    [
        "model",
        "brand",
        "main_color",
        "value",
        "production_cost",
        "transportation_cost",
    ],
)
def test_fields(expected):
    form = CarForm()
    assert expected in list(form.fields)


@pytest.mark.django_db
def test_save_form_creates_car(valid_form):
    valid_form.save()
    assert Car.objects.exists()
