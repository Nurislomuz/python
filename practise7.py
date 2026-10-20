# Practise 7: Smart Home Daily Electricity & Tiered Billing Monitor
# Task: Write a Python program to monitor a household's daily electricity usage (in kWh)
# over N days and compute a tiered utility bill.
#
# The program should:
# 1. Read the number of monitoring days N from the user.
# N must be between 1 and 31 inclusive; otherwise, print 'Invalid number of days' and raise a ValueError.
# 2. Use a loop to read the electricity consumption (in kWh) for each day into a list.
# Use a while loop to ensure each daily reading is between 0.5 kWh and 100.0 kWh inclusive.
# 3. Use a try-except block to handle non-numeric inputs (ValueError).
# 4. Calculate and display the total electricity consumed (kWh) and the average daily consumption (kWh).
# 5. Calculate the Total Electricity Bill ($) using a daily tiered pricing rule:
# for any day where usage is 15.0 kWh or less, that day costs $0.12 per kWh;
# for any day where usage exceeds 15.0 kWh, the entire usage for that day costs $0.20 per kWh.
# 6. Find and display the highest usage, lowest usage, and a list of all readings strictly BELOW the average usage.
# 7. Count and display how many days were 'Eco-Friendly Days' (15.0 kWh or less)
# and how many were 'High-Load Days' (above 15.0 kWh).
# 8. Display whether the household qualifies for the 'Green Home Rebate'
# (granted if Average Daily Usage is 14.0 kWh or less).

days = 0 #between 1 and 31
consumption = []
try:
    days = int(input('Enter the number of monitoring days: ').strip())
    if 1 > days or days > 31 :
        print('Invalid number of days')
        raise ValueError
    for e in range(days):
        con = float(input(f'Enter the electricity consumption (in kWh) for {e+1}days: ').strip())
        if 0.5 > con or con >100:
            print('Invalid electricity consumption')
            raise ValueError
        else:
            consumption.append(con)
    total = sum(consumption)
    average = total/days
except ValueError:
    print('ValueError faced')
else:
    Eco = []
    High = []
    for m in consumption:
        if m < 15:
            Eco.append(m)
        else:
            High.append(m)

    tot_eco = sum(Eco) * 0.12
    tot_high = sum(High) * 0.2
    tot_price = tot_eco + tot_high
    count_Eco = len(Eco)
    count_High = len(High)
    Highest = float(max(consumption))
    Lowest = float(min(consumption))
    below = []
    for b in consumption:
        if b < average:
            below.append(b)
    print()
    print('=' * 10)
    print(f'📆 The number of monitoring days: {days}')
    print(f'🧱 The electricity consumption: {consumption}')
    print(f'🔋 Total electricity consumed: {total:.2f} kWh')
    print(f'🧮 Average electricity consumed per day: {average:.2f} kWh')
    print(f'🏦 Total Electricity Bill: {tot_price:.2f}$')
    print('='*10)
    print(f'🔥 The Highest: {Highest:.2f} kWh')
    print(f'❄️ The Lowest: {Lowest:.2f} kWh')
    print(f'📉 Below than Average: {below}')
    print('=' * 10)
    print(f'🌎 {count_Eco} Eco-Friendly Days: {Eco} ')
    print(f'🚀 {count_High} High-Load Days: {High}')
    if average <= 14:
        print("🎖️The household qualifies for the 'Green Home Rebate'")
finally:
    print('=' * 10)
    print('Program closed')













