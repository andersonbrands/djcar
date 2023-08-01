import pytest

from djcar.core.models import Car

pytestmark = pytest.mark.django_db


@pytest.fixture
def car(valid_car_dict):
    yield Car.objects.create(**valid_car_dict)


def test_create(car):
    assert Car.objects.exists()


def test_str(car):
    assert "Gol - ford (red)" == str(car)
