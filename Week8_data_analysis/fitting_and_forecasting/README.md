# WEEK 8 DATA ANALYSIS, QUALITY AND COMPUTATIONAL COMPLEXITY - FITTING AND FORECASTING
## Overview
This week extended the data analysis techniques to include model fitting and forecasting.  
I worked with a global sea level dataset and explored how different polynomial models fit the data and forecast future values.
I implemented the chi-squared per degree of freedom statistic and used it to compare polynomial models of different orders.

## Files in this folder
- 'fitting_and_forecasting.py' — functions fitting the sea level data and forecasting the last ten years using different polynomials.
- 'reduced_chi_square_vs_degree.png' - plot of chi square fit against polynomial degrees
- 'sea_level_data.csv' - dataset of sea levels over period of time
- 'sea_level_fits_and_forecasts.png' - plot of different polynomials and forecast of last ten years
- 'sea_level_observed_data.png' - the actual sea level data plotted
  
## Results
As the polynomial degree increases, the predicted values for future sea levels becomes more extreme and less reliable
Therefore, lower degree polynomials provide for accurate forecasts

The x**2 per degree of freedom decreased sharply from degree 1 to 2, then levelled off.
This indicates that a second-order polynomial sufficiently captures the trend in global sea-level rise, while higher orders add unnecessary complexity.

## How to run the code
```bash
python Week8_data_analysis/fitting_and_forecasting/fitting_and_forecasting.py
