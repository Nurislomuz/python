# Practise 6: Freelancer Project Earnings & Tax Analysis
# Task: Write a Python program to manage and analyze
# a freelancer's earnings across N completed projects.

# The program should:
# 1. Ask the user to enter the number of completed projects (N).
# If N is 0 or negative, print an error message and raise a ValueError.
# 2. Use a for loop to read the payment amount ($) for each project into a list.
# The minimum allowed fee for any project is $50.0. If the user enters an amount below $50.0, use a while loop to keep prompting until they enter a valid amount ($50.0 or above).
# 3. Wrap the input collection inside a try-except-else-finally block to catch non-numeric entries (ValueError).
# 4. In the else block, calculate and display: Gross Total Earnings,
# a 12% Tax Deduction on the gross total, Net Earnings (Gross - Tax),
# and Average Payment per project (formatted to 2 decimal places).
# 5. Find and display the highest and lowest project payments.
# 6. Categorize all project payments into two separate lists: 'premium_projects' ($500.0 or above) and
# 'standard_projects' (below $500.0). Display both lists along with the count of projects in each category.
# 7. Display whether the freelancer has achieved their financial target.
# The target is met if Net Earnings (after tax) are $2,500.00 or above.
# 8. In the finally block, print a clean separator line and 'Session ended.'

N = 0
payments = []
try:
    N = int(input('Enter the number of completed projects: ').strip())
    if N <= 0:
        print('Invalid value for N')
        raise ValueError
    for s in range(N):
       payment = float(input(f'Enter the amount of payment for {s+1}: ').strip())
       while payment < 50:
        print('Less amount enter more')
        payment = float(input(f'Enter the amount of payment for {s+1}: ').strip())
       payments.append(payment)
except ValueError:
    print('ValueError faced')

else:
    gross_total = sum(payments)
    tax = gross_total * 0.12
    net = gross_total - tax
    average = (gross_total / N)
    highest = max(payments)
    lowest = min(payments)

    premium_projects = []
    standard_projects = []
    for p in payments:
        if p >= 500:
            premium_projects.append(p)
        else:
            standard_projects.append(p)
    print(' ')
    print('-' * 11)
    print(f'The gross total: {gross_total} $')
    print(f'Tax: {tax} $')
    print(f'Net Earnings: {net} $')
    print(f'Average Payment: {average:.2f} $')
    print('-' * 11)
    print(f'Highest: {highest} $\nLowest: {lowest} $')
    print(f'Premium Projects: {premium_projects}')
    print(f'Standart Projects: {standard_projects}')
    print(f'The number of completed projects: {N}')
    print('The target is met' if net > 2500 else 'The target isnt met')
finally:
    print('-'*11)
    print('Session ended.')


