#enter how many days in the month and the starting day of the week
num_days = int(input("Enter number of days in the month (28-31): " ))
start_day = int(input("Enter the starting day of the week (0=Sun, 1=Mon,...6=Sat): " ))

print("S  M  T  W  T  F  S")
#print initial dashes for days before the first
for i in range(start_day):
    print("-", end="  ")
#print the days
for day in range(1, num_days+1):
    print(f"{day:2}", end=" ")
    #print newline after every 7 columns
    if (day + start_day) % 7 == 0:
        print()
print()  #final new line at the end of the month
