import numpy as np
import datetime

today = np.datetime64('today', 'D') #get today's date in YYYY-MM-DD format
user_date = input("Enter a date in YYYY-MM-DD format:") #take user input

difference = np.datetime64(user_date, 'D') - today #calculate difference in days
days_difference = difference.astype(int) #convert to integer
days_difference = abs(days_difference) #get absolute value - no negative days
print(f"The difference is {days_difference} days.") #print the difference
