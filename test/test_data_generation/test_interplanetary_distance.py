import pytest
import pandas as pd
from data_generation.interplanetary_distance import (
    get_interplanetary_distance,
    generate_distances_for_years,
    generate_3_planet_distances_for_years
)


@pytest.mark.parametrize('time_since_start',[0, 584])
@pytest.mark.parametrize('planet_2',['venus','mars'])
@pytest.mark.parametrize('planet_1',['earth'])
def test_distance_t_0(get_planet_parameters,
                      time_since_start,
                      planet_1,
                      planet_2):
    orbital_radius_km_planet_1 = get_planet_parameters[planet_1]['orbital_radius_km']
    orbital_radius_km_planet_2 = get_planet_parameters[planet_2]['orbital_radius_km']
    orbital_period_days_planet_1  = get_planet_parameters[planet_1]['orbital_period_days']
    orbital_period_days_planet_2 = get_planet_parameters[planet_2]['orbital_period_days']
    calculated_distance = get_interplanetary_distance(orbital_radius_km_planet_1,
                                                      orbital_radius_km_planet_2,
                                                      orbital_period_days_planet_1,
                                                      orbital_period_days_planet_2,
                                                      time_since_start)
    expected_distance = orbital_radius_km_planet_1 - orbital_radius_km_planet_2
    #This test currently fails for mars as the calculated distance at 584 days is > 100
    #TODO: We need to determine the periodicity of minima for mars and then parameterize this test appropriately
    # to ensure that it passes
    assert abs(calculated_distance - expected_distance)<100

@pytest.mark.parametrize('num_years',[1, 2, 10])
@pytest.mark.parametrize('planet_2',['venus','mars'])
@pytest.mark.parametrize('planet_1',['earth'])
def test_generation(get_planet_parameters,
                    num_years,
                    planet_1,
                    planet_2):
    orbital_radius_km_planet_1 = get_planet_parameters[planet_1]['orbital_radius_km']
    orbital_radius_km_planet_2 = get_planet_parameters[planet_2]['orbital_radius_km']
    orbital_period_days_planet_1  = get_planet_parameters[planet_1]['orbital_period_days']
    orbital_period_days_planet_2 = get_planet_parameters[planet_2]['orbital_period_days']
    generated_distances = generate_distances_for_years(num_years,
                                                       orbital_radius_km_planet_1,
                                                       orbital_radius_km_planet_2,
                                                       orbital_period_days_planet_1,
                                                       orbital_period_days_planet_2)
    received_length = len(generated_distances)
    expected_length = num_years*365 + int(num_years/4)
    assert received_length == expected_length
    assert type(generated_distances) == pd.DataFrame

@pytest.mark.parametrize('num_years',[1, 2, 10])
@pytest.mark.parametrize('planet_config',[{'anchor_planet':'earth',
                                           'other_planets':['mars','venus']}])
def test_3_planet_distances(num_years,
                            planet_config,
                            get_planet_parameters):
    anchor_planet = planet_config['anchor_planet']
    other_planets = planet_config['other_planets']
    generated_distances = generate_3_planet_distances_for_years(num_years,
                                                                planet_config,
                                                                planet_parameters = get_planet_parameters)
    assert type(generated_distances) == pd.DataFrame
    expected_columns = ['time_since_start',
                        f'inteplanetary_distance_{other_planets[0]}_2_{anchor_planet}',
                        f'inteplanetary_distance_{other_planets[1]}_2_{anchor_planet}',
                        f'sum_other_planets_2_{anchor_planet}']
    assert expected_columns == generated_distances.columns.to_list()
    assert not(any(generated_distances[c] is None for c in expected_columns))
    received_length = len(generated_distances)
    expected_length = num_years*365 + int(num_years/4)
    assert received_length == expected_length