import pytest

from djcar.core.models import Car

pytestmark = pytest.mark.django_db


@pytest.fixture
def car():
    yield Car.objects.create(
        model="Gol",
        brand="ford",
        main_color="red",
        value="50000",
        production_cost="10000",
        transportation_cost="5000",
    )


def test_create(car):
    assert Car.objects.exists()


def test_str(car):
    assert "Gol - ford (red)" == str(car)
