# WEEK 4 PRESENTATIONS, REPORTS AND PROJECT MANAGEMENT

## Overview
This week focused on working in a group to research, analyse, and present evidence on the **Rule of Law** in different countries.  
Our group chose to compare Germany (around the Nazi period) and modern Russia. We created a set of reproducible figures in Python to support the presentation.

## Files in this folder
- 'plot_rol_figures.py' — main script that:
  - loads the rule-of-law data from 'key-features-of-liberal-democracy.csv'
  - cleans and filters the data for Germany and Russia
  - generates and saves all figures used in the presentation
- 'key-features-of-liberal-democracy.csv' — dataset containing rule-of-law index values and related indicators for multiple countries and years
- 'fig1_germany_1930_1950.png' — time series of Germany’s rule-of-law index with key historical events (Hitler’s rise, Nuremberg Laws, WWII, etc.) annotated
- 'fig2_russia_1999_2024.png' — time series of Russia’s rule-of-law index under Putin, with major events marked (economic reforms, protests, Crimea, Ukraine invasion)
- 'fig3_since_regime_start_topbaseline.png' — comparison of absolute change in rule-of-law index since the start of each regime (Germany 1933 vs Russia 1999)
- 'fig3a_since_regime_dual_pct.png' — same as Figure 3 but showing **percentage change**, allowing comparison of relative deterioration
- 'fig4_grouped_pre_vs_war.png' — grouped bar chart comparing pre-war vs war-period average rule-of-law levels in Germany and Russia
- 'fig4a_dual_axis.png' — dual-axis version of Figure 4, showing Germany and Russia on separate y-axes to highlight the different magnitudes of change


## How to run the code
```bash
python Week4_presentations/plot_rol_figures.py
