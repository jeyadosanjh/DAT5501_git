import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

#cleaning cocacola data
df = pd.read_csv('cocacola_data.csv')
df = df.drop(['Volume', 'Open', 'High', 'Low'], axis=1)  # remove unnecessary columns
# converting 'Close/Last' to remove $ sign and convert to float
df['Close/Last'] = df['Close/Last'].replace('[\$,]', '', regex=True).astype(float)

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

#plotting percent change against date
def plot_cocacola_percent_change():
    df['Percent Change'] = df['Close/Last'].pct_change() * 100  #calculate percent change
    plt.plot(pd.to_datetime(df['Date']), df['Percent Change'], label='CocaCola Percent Change', color='orange')
    plt.xlabel('Date')
    plt.ylabel('Percent Change (%)')
    plt.title('CocaCola Asset Percent Change Over Time')
    plt.legend()
    plt.gca().yaxis.set_major_locator(MaxNLocator(integer=True))  # show only whole numbers on y-axis - cleans up y axis
    plt.savefig("cocacola_percent_change.png")
    plt.show()

#calculating standard deviation of percent daily changes
def calculate_std_dev_percent_change():
    std_dev = df['Percent Change'].std()
    print(f"Standard Deviation of Daily Percent Changes: {std_dev:.2f}%")

if __name__ == "__main__":
    plot_cocacola_data()
    plot_cocacola_percent_change()
    calculate_std_dev_percent_change()