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
    # plot the original data
    plt.scatter(df['Year'], df[sea_col], s=10, color='black', label='Observed')

    # fitting polynomials of degree 1..9
    for order in range(1, 10):
        coeffs = np.polyfit(df_subset['Year'], df_subset[sea_col], order)
        # evaluate fit on the full range for plotting
        years_full = np.arange(df['Year'].min(), 2021)
        fit_y = np.polyval(coeffs, years_full)
        plt.plot(years_full, fit_y, label=f'Degree {order} Fit')

        # forecasting 10 years into the future (2011-2020)
        future_years = np.arange(max_fit_year + 1, max_fit_year + 11)
        all_years = np.concatenate((df['Year'].values, future_years))
        # for forecast plotting evaluate on continuous future range
        future_full = np.arange(df['Year'].min(), max_fit_year + 11)
        future_fit_y = np.polyval(coeffs, future_full)
        plt.plot(future_full, future_fit_y, '--', alpha=0.6)

    plt.xlabel('Year')
    plt.ylabel(f'{sea_col}')
    plt.title('Polynomial fits and 10-year forecasts of global sea level')
    plt.legend(ncol=2)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('sea_level_fits_and_forecasts.png')
    plt.show()

def plot_real_data(path='sea_level_data.csv'):
    df, sea_col = load_and_prepare(path)

    plt.figure(figsize=(10, 6))
    # plot the original data
    plt.scatter(df['Year'], df[sea_col], s=10, color='black', label='Observed')

    plt.xlabel('Year')
    plt.ylabel(f'{sea_col}')
    plt.title('Observed Global Sea Level Data')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('sea_level_observed_data.png')
    plt.show()

# Model Testing (x**2 per degree of freedom)

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

if __name__ == '__main__':
    fit_and_plot()
    plot_real_data()
    chi_square_testing()

#RESULTS:
# As the polynomial degree increases, the predicted values for future sea levels becomes more extreme and less reliable
# Therefore, lower degree polynomials provide for accurate forecasts









