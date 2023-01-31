import streamlit as st
import numpy as np
from data_generation.interplanetary_distance import generate_distances_for_years

planet_parameters = {
    'earth': {
        'orbital_period_days': 365.2,
        'orbital_radius_km': 149.6e6
    },
    'venus': {
        'orbital_period_days': 224.7,
        'orbital_radius_km': 108.2e6
    }
}

orbital_radius_km_planet_1 = planet_parameters['earth']['orbital_radius_km']
orbital_radius_km_planet_2 = planet_parameters['venus']['orbital_radius_km']
orbital_period_days_planet_1 = planet_parameters['earth']['orbital_period_days']
orbital_period_days_planet_2 = planet_parameters['venus']['orbital_period_days']

num_years = 10

df =  generate_distances_for_years(num_years,
                                   orbital_radius_km_planet_1,
                                   orbital_radius_km_planet_2,
                                   orbital_period_days_planet_1,
                                   orbital_period_days_planet_2)

st.line_chart(df,
              x='time_since_start',
              y='interplanetary_distance')

st.write(df)
