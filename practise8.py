#  Problem Statement: Write a Python program to create a tuple,
#       access its elements by index, and find its length.
#==================================================================================
# Purpose: This exercise introduces you to the fundamental building blocks of     =
# working with tuples: creating them, retrieving individual elements using        =
# index positions, and measuring their size using len().                          =
# These are the first skills you need before working with any tuple-based data.   =
# Given Input: fruits = ("apple", "banana", "cherry", "date")                     =
#==================================================================================
# Expected Output: First element: apple, Last element: date, and Length: 4

fruits = []
numb = int(input("Enter the number of elements: ").strip())
while 0 > numb:
    print('Invalid number of elements')
    numb = int(input("Enter the number of elements: ").strip())

for i in range(numb):
    s = input(f'Enter the element name for {i+1}: ').strip()
    print(f'{s} added to the list.')
    fruits.append(s)
count = len(fruits) +1
hh = len(fruits)
print(f'First element: {fruits[0]}, Last element: {fruits[-1]}, Length: {count}')
