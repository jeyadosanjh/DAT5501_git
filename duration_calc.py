import numpy as np
import datetime
import pandas as pd

def past_days_csv():
    df = pd.read_csv('random_dates.csv') #read the random dates CSV file
    for x in df['date']:
        date_convert = np.datetime64(x, 'D') #convert to numpy datetime64 object
        today = np.datetime64('today', 'D') #get today's date in YYYY-MM-DD format
        difference = today - date_convert #calculate difference in days
        days_difference = difference.astype(int) #convert to integer
        print(f"Date: {x}, Days from today: {days_difference}") #print the difference


def difference_in_days(user_date):
    today = np.datetime64('today', 'D') #get today's date in YYYY-MM-DD format

    difference = np.datetime64(user_date, 'D') - today #calculate difference in days
    days_difference = difference.astype(int) #convert to integer
    days_difference = abs(days_difference) #get absolute value - no negative days
    return days_difference

if __name__ == "__main__":
    user_date = input("Enter a date in YYYY-MM-DD format:") #take user input
    days_difference = difference_in_days(user_date)
    print(f"The difference is {days_difference} days.") #print the difference
    print("Calculating days difference for dates in random_dates.csv:")
    past_days_csv()
