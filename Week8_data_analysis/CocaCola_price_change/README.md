# WEEK 8 DATA ANALYSIS, QUALITY AND COMPUTATIONAL COMPLEXITY - COCACOLA PRICE CHANGE
## Overview
This week extended the data analysis techniques to include model fitting and forecasting.  
I worked with a global sea level dataset and explored how different polynomial models fit the data and forecast future values.

## Files in this folder
- 'cocacola_asset_price.py' — copy of the functions that create dataset and plot the asset price against date
- 'cocacola_price_sorting.py' - functions that calculate the daily change in price, the time it takes to sort the change in price and plots the change in time against n (7->365)
- 'sort_time_vs_n.png' - plot of the sorting time of daily price changes against n
- 'cocacola_percent_change.png' - plot of the asset percent change over time
  
## Results
Hypothesis: The measured sorting time for T(n) should scale approximately as n log n

Results: The measures sorting time T(n) does scale approximately as n log n, confirming the hypothesis.
Minor deviations at small n arise from timing resolution and system noise

## How to run the code
```bash
python Week8_data_analysis/CocaCola_price_change/cocacola_price_sorting.py
