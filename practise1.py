#Employee Salary Analysis
#Task: Write a Python program to manage an employee's weekly working hours.
#The program should:
#1. Read the working hours for 5 days into a list.
#2. Calculate the total working hours and average working hours.
#3. Display the highest and lowest working hours.
#4. Display whether the employee has completed the required working hours.
#An employee meets the weekly target if the total working hours are 40 or above.

working = []
try:
    worki = int(input('Enter your working day: ').strip())
    if worki <0:
        print('Invalid value')
        raise ValueError
    else:
        print(f'You worked {worki} days')

    for i in range(worki):
        l = int(input('Enter working hours: ').strip())
        if 0>l<24:
            print('Invalid hours')
            raise ValueError
        else:
            working.append(i)
except ValueError:
    print('Program faced ValueError')
else:
    total = sum(working)
    print(f'Total working hours are {total}')
    average = total/worki
    print(f'Your average working hours are {average}')
    highest = max(working)
    lowest = min(working)
    print(f'Your highest working hours are {highest}\n'
          f'Your lowest working hours are {lowest}')
    print('Working hours completed for a week' if total>40
          else 'Working hours arent completed for a week')
finally:
    print('-'*8)