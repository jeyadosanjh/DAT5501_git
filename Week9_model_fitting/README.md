# WEEK 9 MODEL FITTING AND VALIDATION
## Overview
This week built on the sea level forecasting exercise by evaluating which polynomial model is “best”.  
I calculated the BIC and compared to the X** degree of freedom

## Files in this folder
- 'fitting_and_forecasting.py' — I added to the function computing and plotting the BIC for each polynomial order, forecasting ten years with best fit (order 2)
- 'bic_best_model.png' - plot of the best BIC model (order 2) and forecast
- 'bic_vs_degree.png' - plot of BIC against polynomial degree
  
## Results
Comparing BIC to Chi-Square
The plot of BIC and Chi-Square vs Polynomial are similar in shape, both indicating degree 2 as optimal.
Which model is best:
Both BIC and reduced Chi-Square suggest that a polynomial of degree 2 is the best balance between fit quality and model simplicity.

## How to run the code
```bash
python Week8_data_analysis/fitting_and_forecasting/fitting_and_forecasting.py
