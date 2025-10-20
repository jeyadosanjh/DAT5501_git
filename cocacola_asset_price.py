import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

#cleaning cocacola data
df = pd.read_csv('cocacola_data.csv')
df = df.drop(['Volume', 'Open', 'High', 'Low'], axis=1)  # remove unnecessary columns

#plotting closing price against date
def plot_cocacola_data():
    plt.plot(pd.to_datetime(df['Date']), df['Close/Last'], label='CocaCola Closing Price')
    plt.xlabel('Date')
    plt.ylabel('Closing Price')
    plt.title('CocaCola Asset Closing Price Over Time')
    plt.legend()
    plt.gca().yaxis.set_major_locator(MaxNLocator(integer=True))  # show only whole numbers on y-axis - cleans up y axis
    plt.savefig("cocacola_closing_price.png")
    plt.show()

if __name__ == "__main__":
    plot_cocacola_data()
