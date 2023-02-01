import math
import pandas as pd
from .constants import planet_data

def orbital_period_2_angular_velocity(orbital_period_days):
    return 2*math.pi/orbital_period_days

def get_interplanetary_distance(orbital_radius_km_planet_1,
                                orbital_radius_km_planet_2,
                                orbital_period_days_planet_1,
                                orbital_period_days_planet_2,
                                time_since_start):
    orbital_radius_ratio = orbital_radius_km_planet_2/orbital_radius_km_planet_1
    angular_velocity_rad_planet_1 = orbital_period_2_angular_velocity(orbital_period_days_planet_1)
    angular_velocity_rad_planet_2 = orbital_period_2_angular_velocity(orbital_period_days_planet_2)
    squared_distance = (orbital_radius_km_planet_1 ** 2) * \
                       (1 + ((orbital_radius_ratio)**2)
                        - 2*(orbital_radius_ratio)
                        *(math.cos((angular_velocity_rad_planet_2 - angular_velocity_rad_planet_1)*time_since_start)))
    interplanetary_distance = squared_distance**0.5
    return interplanetary_distance

def num_years2num_days(num_years):
    num_days = num_years*365 + int(num_years/4)
    t = range(num_days)
    return t

def generate_distances_for_years(num_years,
                                 orbital_radius_km_planet_1,
                                 orbital_radius_km_planet_2,
                                 orbital_period_days_planet_1,
                                 orbital_period_days_planet_2):
    t = num_years2num_days(num_years)
    distances = [get_interplanetary_distance(orbital_radius_km_planet_1,
                                             orbital_radius_km_planet_2,
                                             orbital_period_days_planet_1,
                                             orbital_period_days_planet_2,
                                             t_x)
                 for t_x in t]
    distances_df = pd.DataFrame({'time_since_start':t,
                                 'interplanetary_distance':distances})
    return distances_df

def generate_3_planet_distances_for_years(num_years,
                                          planet_config,
                                          planet_parameters = planet_data):
    anchor_planet = planet_config['anchor_planet']
    other_planets = planet_config['other_planets']
    t = num_years2num_days(num_years)
    other_planet_distances = [
        generate_distances_for_years(num_years,
                                     planet_parameters[anchor_planet]['orbital_radius_km'],
                                     planet_parameters[other_planet]['orbital_radius_km'],
                                     planet_parameters[anchor_planet]['orbital_period_days'],
                                     planet_parameters[other_planet]['orbital_period_days'])
        for other_planet in other_planets
    ]
    sum_other_distances = other_planet_distances[0]['interplanetary_distance'] + other_planet_distances[1]['interplanetary_distance']
    distances_df = pd.DataFrame({'time_since_start': t,
                                 f'inteplanetary_distance_{other_planets[0]}_2_{anchor_planet}': other_planet_distances[0]['interplanetary_distance'],
                                 f'inteplanetary_distance_{other_planets[1]}_2_{anchor_planet}': other_planet_distances[1]['interplanetary_distance'],
                                 f'sum_other_planets_2_{anchor_planet}': sum_other_distances})
    return distances_df