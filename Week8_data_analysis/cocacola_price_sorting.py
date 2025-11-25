from cocacola_asset_price import df
import pandas as pd
import numpy as np
import time
import matplotlib.pyplot as plt

#change in P= Pn+1 - Pn
#Hypothesis: The measured sorting time for T(n) should scale approximately as n log n

#Results: The measures sorting time T(n) does scale approximately as n log n, confirming the hypothesis.
#Minor deviations at small n arise from timing resolution and system noise

#sorting closing prices and measuring time taken
def sort_cocacola_prices():
    prices = df['Close/Last'].tolist()  # get closing prices as list

    start_time = time.time()
    sorted_prices = sorted(prices)  # sort prices in ascending order
    end_time = time.time()

    time_taken = end_time - start_time
    print(f"Time taken to sort closing prices: {time_taken:.6f} seconds")
    return sorted_prices


# For n = 7->365, time how long it takes to sort the first n daily changes
def time_sort_daily_changes():
    prices = df['Close/Last'].values
    # daily change P_{n+1} - P_n
    daily_changes = prices[1:] - prices[:-1]
    max_n = min(365, len(daily_changes))
    n_values = np.arange(7, max_n + 1)
    times = []
    for n in n_values:
        subset = daily_changes[:n].tolist()
        start = time.time()
        _ = sorted(subset)
        end = time.time()
        times.append(end - start)
    # Plot T vs n and scaled n log n for comparison
    plt.figure()
    plt.plot(n_values, times, marker='o', label='Measured T(n)')
    nlogn = n_values * np.log(n_values)
    # scale nlogn to match the scale of measured times for easier visual comparison
    scale = times[0] / (nlogn[0])
    plt.plot(n_values, scale * nlogn, '--', label=r'scaled $n \log n$')
    plt.xlabel('n (number of daily changes)')
    plt.ylabel('Time to sort (seconds)')
    plt.title('Sorting time of daily price changes vs n')
    plt.legend()
    plt.grid(True)
    plt.savefig('sort_time_vs_n.png')
    plt.show()

if __name__ == "__main__":
    sorted_prices = sort_cocacola_prices()
    print("Sorted Closing Prices:")
    print(sorted_prices)
    time_sort_daily_changes()
