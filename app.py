import streamlit as st
import numpy as np
from data_generation.interplanetary_distance import (
    generate_distances_for_years,
    generate_3_planet_distances_for_years
)
from data_generation.constants import planet_data

anchor_planet = st.selectbox('Select the anchor planet',
                             planet_data.keys())
other_planets = [p for p in planet_data.keys()
                             if p!=anchor_planet]

planet_config = {
    'anchor_planet': anchor_planet,
    'other_planets': other_planets
}

other_planet = st.selectbox('Select the second planet',
                            other_planets)

orbital_radius_km_planet_1 = planet_data[anchor_planet]['orbital_radius_km']
orbital_radius_km_planet_2 = planet_data[other_planet]['orbital_radius_km']
orbital_period_days_planet_1 = planet_data[anchor_planet]['orbital_period_days']
orbital_period_days_planet_2 = planet_data[other_planet]['orbital_period_days']

num_years = st.selectbox("Select the number of years",
                         [10,20,30,40,50])

if st.button("Generate Interplanetary Distance"):

    df =  generate_distances_for_years(num_years,
                                       orbital_radius_km_planet_1,
                                       orbital_radius_km_planet_2,
                                       orbital_period_days_planet_1,
                                       orbital_period_days_planet_2)
    st.title(f"Interplanetary Distance {other_planet} to {anchor_planet} over {num_years} years.")
    st.line_chart(df,
                  x='time_since_start',
                  y='interplanetary_distance')

    st.write(df)

if st.button('Generate 3 Planet Distance'):
    g_t_df = generate_3_planet_distances_for_years(num_years,
                                                   planet_config)
    st.title(f"Interplanetary Distance {other_planets} to {anchor_planet} over {num_years} years.")
    st.line_chart(g_t_df,
                  x='time_since_start')

    st.write(g_t_df)
