import pytest

@pytest.fixture
def get_planet_parameters():
    yield {
        'earth': {
            'orbital_period_days': 365.2,
            'orbital_radius_km': 149.6e6
        },
        'venus': {
            'orbital_period_days': 224.7,
            'orbital_radius_km': 108.2e6
        }
    }