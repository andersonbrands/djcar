import pytest
from django.urls import reverse
from pytest_django.asserts import assertContains, assertTemplateUsed


@pytest.fixture
def add_resp(client):
    url = reverse("add")
    yield client.get(url)


def test_get(add_resp):
    assert 200 == add_resp.status_code


def test_template(add_resp):
    assertTemplateUsed(add_resp, "core/base.html")
    assertTemplateUsed(add_resp, "core/add_car.html")
