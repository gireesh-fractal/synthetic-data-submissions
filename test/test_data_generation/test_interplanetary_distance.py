import pytest
from data_generation.interplanetary_distance import (
    get_interplanetary_distance,
    generate_distances_for_years
)


@pytest.mark.parametrize('time_since_start',[0, 584])
def test_distance_t_0(get_planet_parameters,time_since_start):
    orbital_radius_km_planet_1 = get_planet_parameters['earth']['orbital_radius_km']
    orbital_radius_km_planet_2 = get_planet_parameters['venus']['orbital_radius_km']
    orbital_period_days_planet_1  = get_planet_parameters['earth']['orbital_period_days']
    orbital_period_days_planet_2 = get_planet_parameters['venus']['orbital_period_days']
    calculated_distance = get_interplanetary_distance(orbital_radius_km_planet_1,
                                                      orbital_radius_km_planet_2,
                                                      orbital_period_days_planet_1,
                                                      orbital_period_days_planet_2,
                                                      time_since_start)
    expected_distance = orbital_radius_km_planet_1 - orbital_radius_km_planet_2
    assert abs(calculated_distance - expected_distance)<100

@pytest.mark.parametrize('num_years',[1, 2, 10])
def test_generation(get_planet_parameters,num_years):
    orbital_radius_km_planet_1 = get_planet_parameters['earth']['orbital_radius_km']
    orbital_radius_km_planet_2 = get_planet_parameters['venus']['orbital_radius_km']
    orbital_period_days_planet_1  = get_planet_parameters['earth']['orbital_period_days']
    orbital_period_days_planet_2 = get_planet_parameters['venus']['orbital_period_days']
    generated_distances = generate_distances_for_years(num_years,
                                                       orbital_radius_km_planet_1,
                                                       orbital_radius_km_planet_2,
                                                       orbital_period_days_planet_1,
                                                       orbital_period_days_planet_2)
    received_length = len(generated_distances)
    expected_length = num_years*365 + int(num_years/4)
    assert received_length == expected_length
