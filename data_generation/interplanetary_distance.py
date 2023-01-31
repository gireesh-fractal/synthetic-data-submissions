import math
import pandas as pd

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

def generate_distances_for_years(num_years,
                                 orbital_radius_km_planet_1,
                                 orbital_radius_km_planet_2,
                                 orbital_period_days_planet_1,
                                 orbital_period_days_planet_2):
    num_days = num_years*365 + int(num_years/4)
    t = range(num_days)
    distances = [get_interplanetary_distance(orbital_radius_km_planet_1,
                                             orbital_radius_km_planet_2,
                                             orbital_period_days_planet_1,
                                             orbital_period_days_planet_2,t_x)
                 for t_x in t]
    distances_df = pd.DataFrame({'time_since_start':t,
                                 'interplanetary_distance':distances})
    return distances_df