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
    plt.scatter(data['x'], data['y'], alpha=0.5)
    plt.title('Synthetic Data')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.show()  

if __name__ == "__main__":
    data = generate_synthetic_data()
    plot_data(data)

