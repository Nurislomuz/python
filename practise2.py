#Employee Salary Analysis
#Task: Write a Python program to manage an employee's weekly working hours.
#The program should:
#1. Read the working hours for 5 days into a list.
#2. Calculate the total working hours and average working hours.
#3. Display the highest and lowest working hours.
#4. Display whether the employee has completed the required working hours.
#An employee meets the weekly target if the total working hours are 40 or above.

marks = []
students = 0
try:
    students = int(input('Enter the number of students: ').strip())
    if students <0:
        print('Invalid student number')
        raise ValueError
    for i in range(students):
        l = int(input('Enter mark: ').strip())
        if 100> l <0:
            print('Invalid mark')
            raise ValueError
        else:
            marks.append(l)
    total = sum(marks)
    print('-'*8)
    print(f'Total marks: {total}')
    average = total/students
    print(f'Average marks: {average}')
    highest = max(marks)
    lowest = min(marks)
    print(f'Highest mark: {highest}\nLowest mark: {lowest}')
    print('-' * 8)
except ValueError:
    print('ValueError faced')
else:
    failed = 0
    for s in marks:
        if s < 50:
            failed +=1

    print(f'{failed} students failed')
    passed = 0
    for p in marks:
        if p >= 50:
            passed +=1
    print(f'{passed} students passed')
    print('-'*8)
    greater = []
    for av in marks:
        if av > average:
            greater.append(av)
    print(f'{greater} greater than the average')



