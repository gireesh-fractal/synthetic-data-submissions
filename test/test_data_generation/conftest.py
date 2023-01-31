import pytest
from data_generation.constants import planet_data

@pytest.fixture
def get_planet_parameters():
    yield planet_data