import pytest
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed


@pytest.fixture
def home_resp(client):
    url = reverse("home")
    yield client.get(url)


def test_get(home_resp):
    assert 200 == home_resp.status_code


def test_template(home_resp):
    assertTemplateUsed(home_resp, "core/index.html")
