import pytest
from django.urls import reverse
from pytest_django.asserts import assertContains, assertTemplateUsed

from djcar.core.forms import CarForm


@pytest.fixture
def add_resp(client):
    url = reverse("add")
    yield client.get(url)


def test_get(add_resp):
    assert 200 == add_resp.status_code


def test_template(add_resp):
    assertTemplateUsed(add_resp, "core/base.html")
    assertTemplateUsed(add_resp, "core/add_car.html")


def test_form_in_context(add_resp):
    form = add_resp.context["form"]
    assert isinstance(form, CarForm)


@pytest.mark.parametrize(
    "expected, count",
    [
        # csrf
        ("csrfmiddlewaretoken", 1),
        # form and input tags
        ("<form", 1),
        ("<input", 5),
        ("<select", 2),
        ('type="submit"', 1),
    ],
)
def test_contains(add_resp, expected, count):
    assertContains(add_resp, expected, count)


@pytest.mark.django_db
def test_post_valid(client, valid_car_dict):
    url = reverse("add")
    resp = client.post(url, valid_car_dict, follow=True)
    assertContains(resp, "Success")


@pytest.mark.django_db
def test_post_invalid(client, invalid_car_dict):
    url = reverse("add")
    resp = client.post(url, invalid_car_dict, follow=True)
    assertContains(resp, "Success", count=0)
