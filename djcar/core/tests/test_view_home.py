import pytest
from django.urls import reverse
from pytest_django.asserts import assertContains, assertTemplateUsed

from djcar.core.forms import CarFormSet
from djcar.core.models import Car

pytestmark = pytest.mark.django_db


@pytest.fixture
def home_resp(client):
    url = reverse("home")
    yield client.get(url)


@pytest.fixture
def home_resp_with_car(client, valid_car_dict):
    Car.objects.create(**valid_car_dict)
    url = reverse("home")
    yield client.get(url)


def test_get(home_resp):
    assert 200 == home_resp.status_code


def test_template(home_resp):
    assertTemplateUsed(home_resp, "core/base.html")
    assertTemplateUsed(home_resp, "core/index.html")


@pytest.mark.parametrize(
    "expected",
    [
        # bootstrap
        "https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css",
        "https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/js/bootstrap.bundle.min.js",
        # jquery
        "https://code.jquery.com/jquery-3.7.0.min.js",
        # main css and js
        "css/main.css",
        "js/main.js",
    ],
)
def test_contains(home_resp, expected):
    assertContains(home_resp, expected)


def test_formset(home_resp):
    formset = home_resp.context["formset"]
    assert isinstance(formset, CarFormSet)


def test_no_cars_alert(home_resp, home_resp_with_car):
    text = "No cars registered yet, use the button above to add"
    assertContains(home_resp, text, 1)
    assertContains(home_resp_with_car, text, 0)
