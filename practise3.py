#Practise 3
#Task: Write a Python program to manage a retail store's daily sales revenue for 7 days.

#The program should:
#1. Use a loop to read the daily sales revenue for 7 days from the user and store them in a list.
#2. Use a try-except block to handle non-numeric inputs (ValueError)
# and reject negative sales amounts by prompting the user to re-enter a valid value.
#3. Calculate and display the total weekly sales and average daily sales.
#4. Find and display the highest and lowest daily sales amounts.
#5. Count and display the number of high-sales days ($1,000 or above)
# and low-sales days (below $1,000).
#6. Display whether the store has achieved its weekly sales target.
# A store meets the weekly target if the total sales revenue is $7,000 or above.

days = 0
daily = []
try:
    days = int(input('Enter the number of days: ').strip())
    while days <0:
        print("Invalid number of days")
        days = int(input('Enter the number of days: ').strip())
    else:
        for i in range(days):
          s = float(input('Enter daily sales revenue: ').strip())
          while s == float:
            print("Invalid daily sales revenue")
            s = float(input('Enter daily sales revenue: ').strip())
          else:
            daily.append(s)
except ValueError:
    print('ValueError faced')
else:
    total = sum(daily)
    average = total/days
    print('-'*8)
    print(f'Total: {total}$\nAverage daily: {round(average, 2)}$')
    print('-'*8)
    highest = max(daily)
    lowest = min(daily)

    count = 0
    high_sales= []
    low_sales = []
    for k in daily:
        if k >= 1000:
            high_sales.append(k)
            count+=1
        elif k < 1000:
            low_sales.append(k)
    print(f'The number of high sales day: \n'
          f'High sales: {high_sales}\n'
          f'Low sales: {low_sales}')
    print('-' * 8)
    print('Weekly target achieved' if total>7000
          else 'Weekly target didnt achieved')









