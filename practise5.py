#Task: Write a Python program to manage a delivery vehicle's fuel consumption (in liters)
# across 5 trips.

#The program should:
#1. Read the fuel consumed for 5 trips into a list using a loop.
#2. Use a try-except block to catch non-numeric entries (ValueError)
# and ensure that zero or negative fuel values are not accepted.
#3. Calculate and display the total fuel consumed and average fuel consumption per trip.
#4. Display the highest and lowest fuel consumption amounts.
#5. Display all fuel consumption readings that are greater than the average.
#6. Display whether the driver has met the fuel efficiency target.
#A driver meets the fuel efficiency target if the total fuel consumed for 5 trips is 45 liters or less.

trips = 0
fuel_con = []

try:
    trips = int(input('Enter the number of trips: ').strip())
    if trips <0:
        print('Invalid trips')
        raise ValueError
    for s in range(trips):
        n = float(input(f'Enter fuel consumption for {s+1}: ').strip())
        if n <= 0:
            print(f'Invalid fuel consumption for {s+1}')
            raise ValueError
        else:
            fuel_con.append(n)
except ValueError:
    print('ValueError faced')
else:
    total = sum(fuel_con)
    average = total/trips
    highest = max(fuel_con)
    lowest = min(fuel_con)

    gr = []
    for g in fuel_con:
        if g > average:
            gr.append(g)

    print('-'*8)
    print(f'Total fuel consumption: {total}')
    print(f'Average fuel consumption: {average:.2f}')
    print(f'Highest fuel consumption: {highest}')
    print(f'Lowest fuel consumption: {lowest}')
    print('-' * 8)
    print(f'Greater than average: {gr}')
    print(f'Driver has met the fuel efficiency target' if average <= 5 else "Driver hasn't met the fuel efficiency target")
