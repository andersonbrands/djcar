import pytest


@pytest.fixture
def valid_car_dict():
    yield dict(
        model="Gol",
        brand="ford",
        main_color="red",
        value="50000",
        production_cost="10000",
        transportation_cost="5000",
    )


@pytest.fixture
def invalid_car_dict(valid_car_dict):
    yield dict(
        valid_car_dict,
        **dict(brand="----"),
    )
