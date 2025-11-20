# Found dataset on Sea Level Rises from Our World in Data
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def load_and_prepare(path='sea_level_data.csv'):
    df = pd.read_csv(path)
    # parse Day if present and extract Year
    if 'Day' in df.columns:
        df['Day'] = pd.to_datetime(df['Day'], errors='coerce')
        df['Year'] = df['Day'].dt.year

    # identify averaged sea level column
    avg_col_long = 'Global sea level as an average of Church and White (2011) and UHSLC data'
    if avg_col_long in df.columns:
        df = df.rename(columns={avg_col_long: 'Global sea level (avg)'})

    # prefer the averaged column, otherwise try other common names
    if 'Global sea level (avg)' in df.columns:
        sea_col = 'Global sea level (avg)'
    elif 'CSIRO Adjusted Sea Level (mm)' in df.columns:
        sea_col = 'CSIRO Adjusted Sea Level (mm)'
    else:
        # fall back to the third column if present
        candidate_cols = [c for c in df.columns if 'sea level' in c.lower()]
        if candidate_cols:
            sea_col = candidate_cols[-1]
        else:
            raise ValueError('No sea level column found in CSV')

    # drop rows without year or sea level
    df = df.dropna(subset=['Year', sea_col])
    # ensure numeric
    df[sea_col] = pd.to_numeric(df[sea_col], errors='coerce')
    df = df.dropna(subset=[sea_col])

    return df, sea_col


def fit_and_plot(path='sea_level_data.csv', max_fit_year=2010):
    df, sea_col = load_and_prepare(path)

    # subset for fitting: all years <= max_fit_year
    df_subset = df[df['Year'] <= max_fit_year]

    plt.figure(figsize=(10, 6))
    # estimate observational uncertainty (sigma) from quadratic fit residuals on fit subset
    if len(df_subset) >= 3:
        quad_coeffs = np.polyfit(df_subset['Year'], df_subset[sea_col], 2)
        quad_fit_subset = np.polyval(quad_coeffs, df_subset['Year'])
        sigma = np.std(df_subset[sea_col] - quad_fit_subset)
    else:
        sigma = np.std(df[sea_col].values - np.mean(df[sea_col].values))

    # plot the original data with uncertainty (error bars)
    # plot observed points with light-blue markers and matching error bars
    plt.errorbar(
        df['Year'], df[sea_col], yerr=sigma, fmt='o', markersize=4,
        ecolor='#ADD8E6', elinewidth=1, capsize=2,
        color='#5DADE2', markerfacecolor='#ADD8E6', markeredgecolor='#5DADE2',
        label='Observed ± σ'
    )

    # fitting polynomials of degree 1..9
    cmap = plt.get_cmap('tab10')
    colors = [cmap(i % 10) for i in range(9)]
    for order in range(1, 10):
        coeffs = np.polyfit(df_subset['Year'], df_subset[sea_col], order)
        # evaluate fit on the full range for plotting
        years_full = np.arange(df['Year'].min(), 2021)
        fit_y = np.polyval(coeffs, years_full)
        color = colors[order - 1]
        plt.plot(years_full, fit_y, color=color, linewidth=1.8, label=f'Degree {order} Fit')

        # forecasting 10 years into the future (2011-2020)
        future_full = np.arange(df['Year'].min(), max_fit_year + 11)
        future_fit_y = np.polyval(coeffs, future_full)
        plt.plot(future_full, future_fit_y, '--', color=color, alpha=0.7)

    # mark the year where forecasting begins with a dashed vertical line
    plt.axvline(max_fit_year, color='red', linestyle='--', linewidth=1.2, label='Forecast start')
    # lightly shade the forecast region (next 10 years)
    #plt.axvspan(max_fit_year + 0.01, max_fit_year + 10, color='red', alpha=0.06)

    plt.xlabel('Year')
    plt.ylabel(f'{sea_col}')
    plt.title('Polynomial fits and 10-year forecasts of global sea level')
    plt.legend(ncol=2)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('sea_level_fits_and_forecasts.png')
    plt.show()


# Model Testing (x**2 per degree of freedom) and Bayesian Information Criterion (BIC)

def chi_square_testing(path='sea_level_data.csv', max_fit_year=2010):
    df, sea_col = load_and_prepare(path)

    # subset for fitting: all years <= max_fit_year
    df_subset = df[df['Year'] <= max_fit_year]
    
    x = df_subset['Year'].values
    y = df_subset[sea_col].values
    N0 = len(x)
    sigma = np.std(y - np.mean(y)) * np.ones_like(y)  # assuming constant uncertainty

    for order in range(1, 10):
        coeffs = np.polyfit(df_subset['Year'], df_subset[sea_col], order)
        fit_y_subset = np.polyval(coeffs, df_subset['Year'])
        # Chi Square = Σ((observed - expected)^2 / uncertainty^2)
        chi_square = np.sum(((df_subset[sea_col] - fit_y_subset) ** 2) / (sigma ** 2))
        v = N0 - (order + 1)  # degrees of freedom
        reduced_chi_square = chi_square / v
        print(f'Chi-Square for degree {order}: {chi_square:.2f}, Reduced Chi-Square: {reduced_chi_square:.2f}')

    # plotting x**2 per degree of freedom as function of polynomial degree
    degrees = np.arange(1, 10)
    chi_squares = []
    for order in degrees:
        coeffs = np.polyfit(df_subset['Year'], df_subset[sea_col], order)
        fit_y_subset = np.polyval(coeffs, df_subset['Year'])
        chi_square = np.sum(((df_subset[sea_col] - fit_y_subset) ** 2) / (sigma ** 2))
        v = N0 - (order + 1)
        reduced_chi_square = chi_square / v
        chi_squares.append(reduced_chi_square)
    plt.figure()
    plt.plot(degrees, chi_squares, marker='o')
    plt.xlabel('Polynomial Degree')
    plt.ylabel('Reduced Chi-Square')
    plt.title('Reduced Chi-Square vs Polynomial Degree')
    plt.grid(True)
    plt.savefig('reduced_chi_square_vs_degree.png')
    plt.show()

    # --- New: compute and plot BIC for each polynomial degree (keep reduced chi-square exactly the same) ---
    bics = []
    eps = 1e-12
    for order in degrees:
        coeffs = np.polyfit(df_subset['Year'], df_subset[sea_col], order)
        fit_y_subset = np.polyval(coeffs, df_subset['Year'])
        rss = np.sum((df_subset[sea_col] - fit_y_subset) ** 2)
        k = order + 1  # number of fitted parameters
        bic = N0 * np.log(rss / N0 + eps) + k * np.log(N0)
        bics.append(bic)

    plt.figure()
    plt.plot(degrees, bics, marker='o', color='tab:purple')
    plt.xlabel('Polynomial Degree')
    plt.ylabel('BIC')
    plt.title('Bayesian Information Criterion (BIC) vs Polynomial Degree')
    plt.grid(True)
    plt.savefig('bic_vs_degree.png')
    plt.show()

if __name__ == '__main__':
    fit_and_plot()
    chi_square_testing()

#RESULTS:
# As the polynomial degree increases, the predicted values for future sea levels becomes more extreme and less reliable
# Therefore, lower degree polynomials provide for accurate forecasts

# The x**2 per degree of freedom decreased sharply from degree 1 to 2, then levelled off.
# This indicates that a second-order polynomial sufficiently captures the trend in global sea-level rise, 
# while higher orders add unnecessary complexity.

# Comparing BIC to Chi-Square
# The plot of BIC and Chi-Square vs Polynomial are similar in shape, both indicating degree 2 as optimal.
# Which model is best:
# Both BIC and reduced Chi-Square suggest that a polynomial of degree 2 is the best balance between fit quality and model simplicity.








