import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#plotting histograms of fraction of votes
df = pd.read_csv('US-2016-primary.csv', sep=';')

def plot_histograms():
    plt.hist(df['fraction_votes'], bins=20)
    plt.xlabel('Fraction of Votes')
    plt.ylabel('Count')
    plt.title('Histogram of Fraction of Votes (US 2016 Primary)')
    plt.grid(axis='y', alpha=0.75)
    plt.savefig('us_election_fraction_votes_histogram.png')
    plt.show()


if __name__ == "__main__":
    plot_histograms()
