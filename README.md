# synthetic-data-submissions
My assignment submissions for Dr. Vincent Granville's course on Synthetic Data, Generative and Explainable AI

## Exercise 2.1.1
- Task is to generate 10 yr time series representing the interplanetary distance between Earth and Venus
- data_generation/iterplanetary_distance.py includes the functions to:
  - calculate interplanetary distances for a pair of planets
  - generate a daily time series of distances for a given number of years for a pair of planets
- test module includes some basic tests for this module
- execute `streamlit run app.py` in a venv which has requirements.txt installed in it
- This will bring up a streamlit app in which the generated time series can be visualized both as a line chart and as a dataframe

## Exercise 2.1.2
- Task is to refactor the code in [interpol_fourier.py](https://github.com/VincentGranville/Statistical-Optimization/blob/main/interpol_fourier.py) so that we can perform interpolation on the timeseries generated in the previous task
- This is solved in interpolation/interpol_fourier.py
- At this point the script needs to be manually edited to change the parameters
- By executing the script with n = [8, 16] and t_unit = [32, 64], the interpolated time series and charts found in the .data folder were generated
- Based on manual review of the charts it appears that:
  - We need 32 data points to get a decent performance, errors are significantly higher with 64
  - Using n=16 instead of n=8 results in a shorter time series, but the errors are also lower
- Open questions:
  - What is the intuition behind n i.e the number of nodes?
- Future work if time permits:
  - Modularize the interpolate function so it integrates with data generation functions more intuitively
  - Pull the visualization layer into the streamlit app instead of in the script