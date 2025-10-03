import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random

m = 4.7
b = 0.3
range = 10
num_points = 100

def generate_synthetic_data():
    x = np.linspace(0, range, num_points)
    noise = np.random.normal(0, 1, num_points)
    y = m * x + b + noise
    data = pd.DataFrame({'x': x, 'y': y})
    return data

def plot_data(data):
    # Read data from CSV file
    data = pd.read_csv("synthetic_data.csv")
    plt.scatter(data['x'], data['y'], alpha=0.5, label='Data')
    # Fit a best fit line
    coeffs = np.polyfit(data['x'], data['y'], 1)
    fit_y = np.polyval(coeffs, data['x'])
    plt.plot(data['x'], fit_y, color='red', label=f'Fit: y={coeffs[0]:.2f}x+{coeffs[1]:.2f}')
    # Plot the original input line y = m*x + b
    defined_y = m * data['x'] + b
    plt.plot(data['x'], defined_y, color='green', linestyle='--', label=f'Original Input: y={m}x+{b}')
    plt.title('Synthetic Data with Fitted and Defined Line')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.legend()
    # Save the plot to a file
    plt.savefig("synthetic_plot.png")
    plt.show()

if __name__ == "__main__":
    data = generate_synthetic_data()
    # Save x and y values to a CSV file
    data.to_csv("synthetic_data.csv", index=False)
    plot_data(data)

